const STRIPE_PAYMENT_LINK = 'https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01';

// Normalize a US phone number to E.164 for SMS. Returns null if it can't be done safely.
function toE164(phone) {
  const digits = String(phone).replace(/\D/g, '');
  if (digits.length === 10) return '+1' + digits;
  if (digits.length === 11 && digits.startsWith('1')) return '+' + digits;
  return null;
}

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

    const venmoLink = env.VENMO_HANDLE ? `https://venmo.com/u/${env.VENMO_HANDLE}` : null;

    // 1. ntfy.sh ping (backup channel). The topic is public and readable by
    // anyone who guesses its name, so no lead details go here — just a nudge.
    context.waitUntil(
        fetch('https://ntfy.sh/tennistmate_leads_adeningwerson', {
            method: 'POST',
            headers: {
                'Title': 'New Tennis Booking!',
                'Tags': 'tennis,moneybag'
            },
            body: 'New booking request on tennistmate.com — details in Telegram / admin dashboard.'
        })
    );

    // 2. Telegram ping to Aden (channel of record). Credentials live in
    // Cloudflare Pages env bindings, never in this public repo.
    // Plain text (no parse_mode): user-supplied names must not break delivery.
    if (env.TELEGRAM_BOT_TOKEN && env.TELEGRAM_CHAT_ID) {
      const tgLines = [
        '🎾 NEW TENNIS BOOKING!',
        '',
        '👤 Name: ' + name,
        '📱 Phone: ' + phone,
        '📍 Location: ' + location,
        '⏰ Time: ' + preferred_time,
        '',
        '💳 Payment links (forward to the lead):',
        'Stripe ($25): ' + STRIPE_PAYMENT_LINK
      ];
      if (venmoLink) tgLines.push('Venmo: ' + venmoLink);
      context.waitUntil(
          fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                  chat_id: env.TELEGRAM_CHAT_ID,
                  text: tgLines.join(String.fromCharCode(10))
              })
          })
      );
    }

    // 3. Auto payment message to the lead via SMS. Dormant until the
    // TWILIO_* bindings are configured (Twilio account is Sovereign-gated).
    const smsTo = toE164(phone);
    if (smsTo && env.TWILIO_ACCOUNT_SID && env.TWILIO_AUTH_TOKEN && env.TWILIO_FROM_NUMBER) {
      const smsParts = [
        `Hi ${name}! This is Tennis T-Mate. Got your booking request — I'll be in touch shortly.`,
        `Want to lock in your first lesson now? It's $25:`,
        `Card: ${STRIPE_PAYMENT_LINK}`
      ];
      if (venmoLink) smsParts.push(`Venmo: ${venmoLink}`);
      const smsBody = new URLSearchParams({
        To: smsTo,
        From: env.TWILIO_FROM_NUMBER,
        Body: smsParts.join(String.fromCharCode(10))
      });
      context.waitUntil(
          fetch(`https://api.twilio.com/2010-04-01/Accounts/${env.TWILIO_ACCOUNT_SID}/Messages.json`, {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/x-www-form-urlencoded',
                  'Authorization': 'Basic ' + btoa(env.TWILIO_ACCOUNT_SID + ':' + env.TWILIO_AUTH_TOKEN)
              },
              body: smsBody
          })
      );
    }

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
