export async function onRequestGet(context) {
    const { env } = context;
    try {
        const { results } = await env.DB.prepare("SELECT id, email FROM users ORDER BY created_at DESC").all();
        return new Response(JSON.stringify({ success: true, users: results }), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 });
    }
}
