export async function onRequestGet(context) {
    const { request, env } = context;
    const pin = request.headers.get('X-Admin-Pin');
    if (pin !== '1743') {
        return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
    }

    try {
        const { results } = await env.DB.prepare("SELECT id, email FROM users ORDER BY created_at DESC").all();
        return new Response(JSON.stringify({ success: true, users: results }), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 });
    }
}
