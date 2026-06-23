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

    // 1. Existing ntfy.sh ping
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

    // 2. New Telegram Bot ping directly to Aden's private messages
    const tgMessage = `🎾 *NEW TENNIS BOOKING!*\n\n👤 *Name:* ${name}\n📱 *Phone:* ${phone}\n📍 *Location:* ${location}\n⏰ *Time:* ${preferred_time}\n\n_Generated via tennistmate.com_`;
    
    context.waitUntil(
        fetch('https://api.telegram.org/bot8693402022:AAEwxx69l0VRy-BoHB4b24iEojIUfqKkUNs/sendMessage', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                chat_id: "6378225299",
                text: tgMessage,
                parse_mode: "Markdown"
            })
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
