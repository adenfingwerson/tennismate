export async function onRequestPost(context) {
    const { request, env } = context;
    const pin = request.headers.get('X-Admin-Pin');
    if (pin !== '1743') {
        return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
    }

    try {
        const body = await request.json();
        const name = body.name;

        if (!name) {
            return new Response(JSON.stringify({ error: 'Player name is required' }), { status: 400 });
        }

        // Generate a random UUID
        const id = crypto.randomUUID();
        
        // Since email is UNIQUE NOT NULL in the database, we generate a dummy one
        // so the coach can create a player just by their name.
        const dummyEmail = `player_${id}@placeholder.tennistmate.com`;

        // 1. Insert into users table
        await env.DB.prepare("INSERT INTO users (id, email) VALUES (?, ?)")
            .bind(id, dummyEmail).run();

        // 2. Insert into player_metrics table with the name as field_0
        // (field_0 maps to the #profile-name input on the frontend)
        const metricsObj = { field_0: name };
        await env.DB.prepare("INSERT INTO player_metrics (user_id, metrics_json) VALUES (?, ?)")
            .bind(id, JSON.stringify(metricsObj)).run();

        return new Response(JSON.stringify({ success: true, id: id }), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 });
    }
}
