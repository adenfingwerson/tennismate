export async function onRequestPost(context) {
    const { request, env } = context;
    try {
        const body = await request.json();
        const email = body.email;
        const phone = body.phone_number || null;

        if (!email) {
            return new Response(JSON.stringify({ error: 'Email is required' }), { status: 400 });
        }

        // Check if user exists
        let { results } = await env.DB.prepare("SELECT * FROM users WHERE email = ?").bind(email).all();
        let user = results[0];

        if (!user) {
            // Create new user
            const id = crypto.randomUUID();
            await env.DB.prepare("INSERT INTO users (id, email, phone_number) VALUES (?, ?, ?)")
                .bind(id, email, phone).run();
            user = { id, email, phone_number: phone };
        } else if (phone && !user.phone_number) {
            // Update phone number if it's a lead capture upgrade
            await env.DB.prepare("UPDATE users SET phone_number = ? WHERE id = ?").bind(phone, user.id).run();
            user.phone_number = phone;
        }

        return new Response(JSON.stringify({ success: true, user }), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 });
    }
}
