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

        const { results: profileResults } = await env.DB.prepare("SELECT metrics_json FROM player_metrics WHERE user_id = ?").bind(userId).all();
        
        const { results: lessonResults } = await env.DB.prepare("SELECT raw_notes FROM lessons WHERE user_id = ? ORDER BY created_at DESC LIMIT 5").bind(userId).all();
        const pastNotes = lessonResults.map(l => l.raw_notes).join(' | ');

        if (!pastNotes) {
            return new Response(JSON.stringify({ error: 'No lesson notes found for this player. Log a lesson first.' }), { status: 400 });
        }

        const prompt = "You are an elite tennis tactician applying Cognitive Simplicity principles. Based on the coach's recent notes: " + pastNotes + " Output a strictly formatted JSON object (no markdown, no backticks, ONLY raw JSON) containing exactly 3 keys for the player's tactical blueprint: 1. 'core_focus': A hyper-simple 1-sentence main goal. 2. 'mechanical_cues': An array of exactly 3 simple strings (e.g. 'Low-to-high on FH', 'Loose grip on serve'). 3. 'tactical_rule': One strict, non-negotiable rule to play by (e.g. 'Get it back one more time than them'). Do NOT include any extra text outside the JSON.";

        const response = await env.AI.run('@cf/meta/llama-3.1-8b-instruct-fp8', {
            messages: [{ role: 'user', content: prompt }]
        });
        
        let aiText = response.response;
        
        let aiData = {
            core_focus: "Awaiting analysis...",
            mechanical_cues: ["Awaiting data..."],
            tactical_rule: "Awaiting data..."
        };
        
        try {
            const jsonStart = aiText.indexOf('{');
            const jsonEnd = aiText.lastIndexOf('}');
            if (jsonStart !== -1 && jsonEnd !== -1) {
                aiData = JSON.parse(aiText.substring(jsonStart, jsonEnd + 1));
            }
        } catch (e) {
            console.error("Failed to parse AI JSON output");
        }

        let metricsObj = {};
        if (profileResults.length > 0 && profileResults[0].metrics_json) {
            try {
                metricsObj = JSON.parse(profileResults[0].metrics_json);
            } catch(e) {}
        }
        
        metricsObj.ai_focus = aiData.core_focus;
        metricsObj.ai_cues = aiData.mechanical_cues;
        metricsObj.ai_rule = aiData.tactical_rule;

        await env.DB.prepare(`
            INSERT INTO player_metrics (user_id, metrics_json) VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET metrics_json = excluded.metrics_json, last_updated = CURRENT_TIMESTAMP
        `).bind(userId, JSON.stringify(metricsObj)).run();

        return new Response(JSON.stringify({ success: true, ai_plan: aiData }), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 });
    }
}
