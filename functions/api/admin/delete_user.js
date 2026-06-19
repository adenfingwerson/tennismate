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

        // Safeguard: Prevent deleting the admin account
        const { results } = await env.DB.prepare("SELECT email FROM users WHERE id = ?").bind(userId).all();
        if (results.length > 0 && results[0].email.toLowerCase() === 'aden.f.ingwerson@gmail.com') {
            return new Response(JSON.stringify({ error: 'Cannot delete the admin account.' }), { status: 403 });
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