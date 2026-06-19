export async function onRequestPost(context) {
    const { request, env } = context;
    const pin = request.headers.get('X-Admin-Pin');
    if (pin !== '1743') {
        return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
    }

    try {
        const body = await request.json();
        const userId = body.user_id;

        if (!userId) {
            return new Response(JSON.stringify({ error: 'User ID is required' }), { status: 400 });
        }

        // 1. Fetch Player Profile
        const { results: profileResults } = await env.DB.prepare("SELECT metrics_json FROM player_metrics WHERE user_id = ?").bind(userId).all();
        const profile = profileResults.length > 0 ? profileResults[0].metrics_json : "No profile data filled yet.";

        // 2. Fetch Latest Lesson Notes
        const { results: lessonResults } = await env.DB.prepare("SELECT raw_notes FROM lessons WHERE user_id = ? ORDER BY created_at DESC LIMIT 5").bind(userId).all();
        const pastNotes = lessonResults.map(l => l.raw_notes).join("\\n\\n");

        if (!pastNotes) {
            return new Response(JSON.stringify({ error: 'No lesson notes found for this player. Log a lesson first.' }), { status: 400 });
        }

        // 3. Construct AI Prompt
        const prompt = `You are an elite tennis tactician. Based on the player's base profile and the coach's recent lesson notes, generate a strict, highly condensed tactical blueprint.
        
        Player Profile (JSON): ${profile}
        Recent Coach Notes: ${pastNotes}
        
        Return exactly 3 lines of text, formatted exactly like this:
        A-GAME: [1-2 punch based on their strengths]
        VULNERABILITY: [What breaks down, based on coach notes]
        RESET TRIGGER: [A mental or physical cue to fix the vulnerability]
        
        Keep it extremely brutalist, tactical, and short. Do not include any other conversational text.`;

        // 4. Run Cloudflare Workers AI
        const response = await env.AI.run('@cf/meta/llama-3.1-8b-instruct-fp8', {
            messages: [{ role: 'user', content: prompt }]
        });
        
        let aiText = response.response;
        
        // Try to parse the response and update the profile automatically
        const lines = aiText.split('\n').filter(l => l.trim().length > 0);
        let a_game = "", vuln = "", reset = "";
        
        lines.forEach(line => {
            if (line.toUpperCase().includes('A-GAME:')) a_game = line.split(':')[1].trim();
            if (line.toUpperCase().includes('VULNERABILITY:')) vuln = line.split(':')[1].trim();
            if (line.toUpperCase().includes('RESET TRIGGER:')) reset = line.split(':')[1].trim();
        });

        // Save back to D1 under the user's metrics_json
        let metricsObj = {};
        if (profileResults.length > 0 && profileResults[0].metrics_json) {
            try {
                metricsObj = JSON.parse(profileResults[0].metrics_json);
            } catch(e) {}
        }
        
        // Add the AI data to the object
        metricsObj.ai_a_game = a_game || aiText.substring(0, 100); 
        metricsObj.ai_vuln = vuln || "";
        metricsObj.ai_reset = reset || "";

        // Upsert back to database
        await env.DB.prepare(`
            INSERT INTO player_metrics (user_id, metrics_json) VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET metrics_json = excluded.metrics_json, last_updated = CURRENT_TIMESTAMP
        `).bind(userId, JSON.stringify(metricsObj)).run();

        return new Response(JSON.stringify({ success: true, ai_plan: aiText }), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 });
    }
}