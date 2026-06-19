import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Add modal CSS
modal_css = """
        /* Booking Modal */
        .modal-overlay { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.8); z-index: 999; align-items: center; justify-content: center; backdrop-filter: blur(5px); }
        .modal-content { background: var(--bg); color: var(--text); padding: 40px; border-radius: 12px; width: 100%; max-width: 500px; border: 1px solid var(--border-dark); position: relative; }
        .modal-close { position: absolute; top: 16px; right: 20px; font-size: 1.5rem; cursor: pointer; font-weight: 900; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 8px; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; }
        .form-group input, .form-group select { width: 100%; padding: 12px; border: 1px solid var(--border-dark); border-radius: 4px; font-family: inherit; font-size: 1rem; }
        .modal-btn { width: 100%; padding: 16px; background: var(--accent); color: var(--text); font-weight: 900; text-transform: uppercase; border: 2px solid var(--text); font-size: 1.1rem; cursor: pointer; transition: all 0.2s; }
        .modal-btn:hover { background: var(--text); color: var(--bg); }
"""
html = html.replace('</style>', modal_css + '\n    </style>')

# 2. Add modal HTML right after <body>
modal_html = """
    <div class="modal-overlay" id="bookingModal">
        <div class="modal-content">
            <div class="modal-close" onclick="closeModal()">&times;</div>
            <h2 style="margin-bottom: 8px;">Schedule Lesson</h2>
            <p style="color: var(--text-muted); margin-bottom: 24px; font-size: 0.95rem;">Pick your preferred time. You'll be redirected to Stripe to lock it in.</p>
            
            <form id="bookingForm" onsubmit="submitBooking(event)">
                <div class="form-group">
                    <label>Full Name</label>
                    <input type="text" id="b_name" required>
                </div>
                <div class="form-group">
                    <label>Phone Number (For Texting)</label>
                    <input type="tel" id="b_phone" required>
                </div>
                <div class="form-group">
                    <label>Location</label>
                    <select id="b_location" required>
                        <option value="Holdrege">Holdrege, NE (Mon-Sun)</option>
                        <option value="Hastings">Hastings, NE (Thursdays)</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Preferred Day & Time</label>
                    <input type="text" id="b_time" placeholder="e.g., Tuesday at 4:30 PM" required>
                </div>
                <button type="submit" class="modal-btn" id="b_submit">Continue to Payment &rarr;</button>
            </form>
        </div>
    </div>
"""
html = html.replace('<body>', '<body>\n' + modal_html)

# 3. Change Stripe Links to Open Modal
html = html.replace('href="https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01"', 'href="#" onclick="openModal(event)"')

# 4. Add Javascript
script_js = """
        // Booking Modal Logic
        function openModal(e) {
            if(e) e.preventDefault();
            document.getElementById('bookingModal').style.display = 'flex';
        }
        function closeModal() {
            document.getElementById('bookingModal').style.display = 'none';
        }
        
        async function submitBooking(e) {
            e.preventDefault();
            const btn = document.getElementById('b_submit');
            btn.innerText = "Processing...";
            btn.disabled = true;

            const payload = {
                name: document.getElementById('b_name').value,
                phone: document.getElementById('b_phone').value,
                location: document.getElementById('b_location').value,
                preferred_time: document.getElementById('b_time').value
            };

            try {
                const res = await fetch('/api/book', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(payload)
                });
                
                if (res.ok) {
                    // Redirect to Stripe immediately after saving the lead
                    window.location.href = "https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01";
                } else {
                    alert("Error saving request. Taking you to checkout anyway.");
                    window.location.href = "https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01";
                }
            } catch (err) {
                window.location.href = "https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01";
            }
        }
"""
html = html.replace('</script>', script_js + '\n    </script>')

with open('index.html', 'w') as f:
    f.write(html)
