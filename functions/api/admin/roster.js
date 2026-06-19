export async function onRequestGet(context) {
    const { request, env } = context;
    const pin = request.headers.get('X-Admin-Pin');
    if (pin !== '1743') {
        return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
    }

    try {
        const { results } = await env.DB.prepare(`
            SELECT u.id, u.email, p.metrics_json 
            FROM users u 
            LEFT JOIN player_metrics p ON u.id = p.user_id 
            WHERE LOWER(u.email) != 'aden.f.ingwerson@gmail.com' 
            ORDER BY u.created_at DESC
        `).all();
        return new Response(JSON.stringify({ success: true, users: results }), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 });
    }
}
