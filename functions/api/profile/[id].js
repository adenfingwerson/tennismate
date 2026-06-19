export async function onRequestGet(context) {
    const { params, env } = context;
    const userId = params.id;
    try {
        const { results } = await env.DB.prepare("SELECT * FROM player_metrics WHERE user_id = ?").bind(userId).all();
        const metrics = results.length > 0 ? results[0].metrics_json : null;
        
        return new Response(JSON.stringify({ success: true, metrics }), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 });
    }
}

export async function onRequestPost(context) {
    const { request, params, env } = context;
    const userId = params.id;
    try {
        const metricsJson = await request.text();
        
        // Upsert metrics
        await env.DB.prepare(`
            INSERT INTO player_metrics (user_id, metrics_json) VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET metrics_json = excluded.metrics_json, last_updated = CURRENT_TIMESTAMP
        `).bind(userId, metricsJson).run();
        
        return new Response(JSON.stringify({ success: true }), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 });
    }
}
