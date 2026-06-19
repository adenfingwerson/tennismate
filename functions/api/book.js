export async function onRequestPost(context) {
  try {
    const { request, env } = context;
    const data = await request.json();
    
    const name = data.name;
    const phone = data.phone;
    const location = data.location;
    const preferred_time = data.preferred_time;

    if (!name || !phone || !location || !preferred_time) {
      return new Response(JSON.stringify({ error: 'Missing required fields' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const { success } = await env.DB.prepare(
      "INSERT INTO booking_requests (name, phone, location, preferred_time, status) VALUES (?, ?, ?, ?, 'pending')"
    ).bind(name, phone, location, preferred_time).run();

    const lines = ["Name: " + name, "Phone: " + phone, "Location: " + location, "Time: " + preferred_time];

    context.waitUntil(
        fetch('https://ntfy.sh/tennistmate_leads_adeningwerson', {
            method: 'POST',
            headers: {
                'Title': 'New Tennis Booking!',
                'Tags': 'tennis,moneybag'
            },
            body: lines.join(String.fromCharCode(10))
        })
    );

    if (success) {
      return new Response(JSON.stringify({ success: true, message: 'Booking saved' }), {
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