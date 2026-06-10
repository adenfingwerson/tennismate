export async function onRequestPost(context) {
  try {
    const { request, env } = context;
    
    // Parse the JSON payload
    const data = await request.json();
    const email = data.email;
    const source = data.source || 'website';
    
    if (!email || !email.includes('@')) {
      return new Response(JSON.stringify({ error: 'Invalid email address' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Insert into D1 Database
    const { success } = await env.DB.prepare(
      'INSERT OR IGNORE INTO subscribers (email, source) VALUES (?, ?)'
    ).bind(email, source).run();

    if (success) {
      return new Response(JSON.stringify({ success: true, message: 'Subscribed successfully!' }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });
    } else {
      throw new Error('Database insertion failed');
    }
    
  } catch (err) {
    return new Response(JSON.stringify({ error: err.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
