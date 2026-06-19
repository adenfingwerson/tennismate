export async function onRequestPost(context) {
    const { request, env } = context;
    try {
        const body = await request.json();
        const id = crypto.randomUUID();
        
        await env.DB.prepare("INSERT INTO lessons (id, user_id, lesson_date, raw_notes) VALUES (?, ?, ?, ?)")
            .bind(id, body.user_id, body.lesson_date, body.raw_notes).run();
            
        return new Response(JSON.stringify({ success: true }), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 });
    }
}
