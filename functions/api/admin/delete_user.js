export async function onRequestPost(context) {
    const { request, env } = context;
    try {
        const body = await request.json();
        const userId = body.user_id;

        if (!userId) {
            return new Response(JSON.stringify({ error: 'User ID is required' }), { status: 400 });
        }

        // Delete from all tables to maintain referential integrity
        await env.DB.prepare("DELETE FROM lessons WHERE user_id = ?").bind(userId).run();
        await env.DB.prepare("DELETE FROM player_metrics WHERE user_id = ?").bind(userId).run();
        await env.DB.prepare("DELETE FROM users WHERE id = ?").bind(userId).run();
            
        return new Response(JSON.stringify({ success: true }), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 });
    }
}