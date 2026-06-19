import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. CSS Additions for Progressive Disclosure & Multi-step Modal
css_additions = """
        /* Progressive Disclosure Accordions */
        .accordion {
            border-bottom: 1px solid var(--border-dark);
        }
        .accordion-header {
            width: 100%;
            text-align: left;
            padding: 32px 0;
            background: none;
            border: none;
            font-size: 2.5rem;
            font-weight: 900;
            text-transform: uppercase;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: var(--text);
            transition: color 0.2s;
        }
        .accordion-header:hover {
            color: var(--text-muted);
        }
        .accordion-icon {
            font-size: 2rem;
            font-weight: 400;
            transition: transform 0.3s ease;
        }
        .accordion.active .accordion-icon {
            transform: rotate(45deg);
        }
        .accordion-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease-out, padding 0.4s ease-out;
            opacity: 0;
        }
        .accordion.active .accordion-content {
            max-height: 1000px; /* arbitrary large number */
            padding-bottom: 32px;
            opacity: 1;
            transition: max-height 0.5s ease-in, padding 0.5s ease-in, opacity 0.5s ease-in;
        }

        /* Modern Multi-Step Booking Modal */
        .modal-overlay { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.85); z-index: 9999; align-items: center; justify-content: center; backdrop-filter: blur(10px); }
        .modal-content { background: var(--bg); color: var(--text); padding: 48px; border-radius: 16px; width: 100%; max-width: 550px; border: 1px solid var(--border-dark); position: relative; overflow: hidden;}
        .modal-close { position: absolute; top: 20px; right: 24px; font-size: 2rem; cursor: pointer; font-weight: 400; line-height: 1; color: var(--text-muted); }
        .modal-close:hover { color: var(--text); }
        
        .step-indicator { display: flex; gap: 8px; margin-bottom: 32px; }
        .step-dot { height: 4px; flex: 1; background: var(--border); border-radius: 2px; transition: background 0.3s; }
        .step-dot.active { background: var(--text); }
        
        .booking-step { display: none; animation: slideIn 0.3s ease forwards; }
        .booking-step.active { display: block; }
        @keyframes slideIn { from { opacity: 0; transform: translateX(20px); } to { opacity: 1; transform: translateX(0); } }

        .modal-title { font-size: 2rem; margin-bottom: 8px; line-height: 1.1; }
        .modal-subtitle { color: var(--text-muted); margin-bottom: 32px; font-size: 1rem; }

        .form-group { margin-bottom: 24px; }
        .form-group label { display: block; margin-bottom: 8px; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.05em; }
        .form-group input, .form-group select { width: 100%; padding: 16px; border: 1px solid var(--border-dark); border-radius: 8px; font-family: inherit; font-size: 1.1rem; background: var(--bg); color: var(--text); outline: none; transition: border-color 0.2s; }
        .form-group input:focus, .form-group select:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(204,255,0,0.2); }
        
        .radio-group { display: grid; grid-template-columns: 1fr; gap: 12px; }
        .radio-option { border: 1px solid var(--border-dark); border-radius: 8px; padding: 16px; cursor: pointer; transition: all 0.2s; display: flex; flex-direction: column; }
        .radio-option:hover { border-color: var(--text); background: #f9f9f9; }
        .radio-option.selected { border-color: var(--text); border-width: 2px; background: var(--text); color: var(--bg); }
        .radio-option-title { font-weight: 900; font-size: 1.1rem; text-transform: uppercase; margin-bottom: 4px; }
        .radio-option-desc { font-size: 0.9rem; color: var(--text-muted); }
        .radio-option.selected .radio-option-desc { color: #aaaaaa; }

        .modal-actions { display: flex; gap: 16px; margin-top: 40px; }
        .btn-modal { flex: 1; padding: 16px; font-weight: 900; text-transform: uppercase; letter-spacing: 0.05em; font-size: 1rem; cursor: pointer; border-radius: 8px; border: none; transition: all 0.2s; }
        .btn-next { background: var(--text); color: var(--bg); }
        .btn-next:hover { background: #333; }
        .btn-prev { background: transparent; color: var(--text); border: 1px solid var(--border-dark); }
        .btn-prev:hover { background: #f5f5f5; }
        .btn-submit { background: var(--accent); color: var(--text); border: 2px solid var(--text); box-shadow: 4px 4px 0 var(--border-dark); }
        .btn-submit:hover { transform: translate(2px, 2px); box-shadow: 2px 2px 0 var(--border-dark); }
"""
html = html.replace('</style>', css_additions + '\n    </style>')

# 2. Extract and replace the 3 sections with Progressive Disclosure accordions
roster_match = re.search(r'<section class="roster">.*?</section>', html, re.DOTALL)
packages_match = re.search(r'<section class="packages">.*?</section>', html, re.DOTALL)
logistics_match = re.search(r'<section class="logistics">.*?</section>', html, re.DOTALL)

if roster_match and packages_match and logistics_match:
    # Get inner content of each section
    roster_content = re.search(r'<div class="section-content">(.*?)</div>\s*</div>\s*</section>', roster_match.group(0), re.DOTALL).group(1)
    packages_content = re.search(r'<div class="section-content">(.*?)</div>\s*</div>\s*</section>', packages_match.group(0), re.DOTALL).group(1)
    logistics_content = re.search(r'<div class="section-content location-grid">(.*?)</div>\s*</div>\s*</section>', logistics_match.group(0), re.DOTALL).group(1)

    progressive_html = f"""
    <section class="details-accordion" style="padding: 60px 0;">
        <div class="container" style="max-width: 800px;">
            
            <div class="accordion">
                <button class="accordion-header" onclick="toggleAccordion(this)">
                    The Roster
                    <span class="accordion-icon">+</span>
                </button>
                <div class="accordion-content">
                    {roster_content}
                </div>
            </div>

            <div class="accordion">
                <button class="accordion-header" onclick="toggleAccordion(this)">
                    Pricing & Rates
                    <span class="accordion-icon">+</span>
                </button>
                <div class="accordion-content">
                    <div style="padding-top: 16px;">
                    {packages_content}
                    </div>
                </div>
            </div>

            <div class="accordion">
                <button class="accordion-header" onclick="toggleAccordion(this)">
                    Locations
                    <span class="accordion-icon">+</span>
                </button>
                <div class="accordion-content">
                    <div class="location-grid" style="padding-top: 16px;">
                    {logistics_content}
                    </div>
                </div>
            </div>

        </div>
    </section>
    """
    # Replace the old sections with the progressive disclosure one
    # We replace the first one with the new html, and replace the other two with empty string
    html = html.replace(roster_match.group(0), progressive_html)
    html = html.replace(packages_match.group(0), "")
    html = html.replace(logistics_match.group(0), "")

# 3. Inject the Multi-Step Modal HTML right after <body>
modal_html = """
    <!-- Multi-Step Booking Flow -->
    <div class="modal-overlay" id="bookingModal">
        <div class="modal-content">
            <div class="modal-close" onclick="closeModal()">&times;</div>
            
            <div class="step-indicator">
                <div class="step-dot active" id="dot-1"></div>
                <div class="step-dot" id="dot-2"></div>
                <div class="step-dot" id="dot-3"></div>
            </div>

            <form id="bookingForm" onsubmit="submitBooking(event)">
                
                <!-- STEP 1: Location -->
                <div class="booking-step active" id="step-1">
                    <h2 class="modal-title">Where do you want to hit?</h2>
                    <p class="modal-subtitle">Select a location to continue.</p>
                    
                    <div class="radio-group">
                        <div class="radio-option selected" onclick="selectRadio('location', 'Holdrege', this)">
                            <span class="radio-option-title">Holdrege, NE</span>
                            <span class="radio-option-desc">North Park Courts • Available Mon - Sun</span>
                        </div>
                        <div class="radio-option" onclick="selectRadio('location', 'Hastings', this)">
                            <span class="radio-option-title">Hastings, NE</span>
                            <span class="radio-option-desc">Hastings College • Available Thursdays Only</span>
                        </div>
                    </div>
                    <input type="hidden" id="b_location" value="Holdrege">
                    
                    <div class="modal-actions">
                        <button type="button" class="btn-modal btn-next" onclick="nextStep(2)">Continue &rarr;</button>
                    </div>
                </div>

                <!-- STEP 2: Time -->
                <div class="booking-step" id="step-2">
                    <h2 class="modal-title">When works for you?</h2>
                    <p class="modal-subtitle">Propose a day and time. We'll finalize via text.</p>
                    
                    <div class="form-group">
                        <label>Preferred Day & Time</label>
                        <input type="text" id="b_time" placeholder="e.g., Tuesday at 4:30 PM" required>
                    </div>
                    
                    <div class="modal-actions">
                        <button type="button" class="btn-modal btn-prev" onclick="nextStep(1)">&larr; Back</button>
                        <button type="button" class="btn-modal btn-next" onclick="nextStep(3)">Continue &rarr;</button>
                    </div>
                </div>

                <!-- STEP 3: Contact & Payment -->
                <div class="booking-step" id="step-3">
                    <h2 class="modal-title">Final Details</h2>
                    <p class="modal-subtitle">Enter your contact info. You'll be redirected to Stripe to lock in the $25.</p>
                    
                    <div class="form-group">
                        <label>Full Name</label>
                        <input type="text" id="b_name" placeholder="John Doe" required>
                    </div>
                    <div class="form-group">
                        <label>Phone Number</label>
                        <input type="tel" id="b_phone" placeholder="(555) 123-4567" required>
                    </div>
                    
                    <div class="modal-actions">
                        <button type="button" class="btn-modal btn-prev" onclick="nextStep(2)">&larr; Back</button>
                        <button type="submit" class="btn-modal btn-submit" id="b_submit">Pay $25 on Stripe &rarr;</button>
                    </div>
                </div>

            </form>
        </div>
    </div>
"""
html = html.replace('<body>', '<body>\n' + modal_html)

# 4. Replace Stripe Links with Modal Triggers
html = html.replace('href="https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01"', 'href="#" onclick="openModal(event)"')

# 5. Add JS logic
script_js = """
        // Progressive Disclosure Accordion Logic
        function toggleAccordion(btn) {
            const accordion = btn.parentElement;
            accordion.classList.toggle('active');
        }

        // Multi-Step Booking Modal Logic
        function openModal(e) {
            if(e) e.preventDefault();
            document.getElementById('bookingModal').style.display = 'flex';
            // Reset to step 1
            nextStep(1);
            document.body.style.overflow = 'hidden';
        }
        function closeModal() {
            document.getElementById('bookingModal').style.display = 'none';
            document.body.style.overflow = 'auto';
        }
        
        function selectRadio(field, value, el) {
            document.getElementById('b_' + field).value = value;
            const siblings = el.parentElement.children;
            for(let i=0; i<siblings.length; i++) {
                siblings[i].classList.remove('selected');
            }
            el.classList.add('selected');
        }

        function nextStep(step) {
            // Basic validation before moving forward
            if(step === 3) {
                if(!document.getElementById('b_time').value.trim()) {
                    alert('Please enter a preferred time.');
                    return;
                }
            }

            document.querySelectorAll('.booking-step').forEach(el => el.classList.remove('active'));
            document.getElementById('step-' + step).classList.add('active');
            
            document.querySelectorAll('.step-dot').forEach((el, index) => {
                if (index < step) el.classList.add('active');
                else el.classList.remove('active');
            });
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
                    window.location.href = "https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01";
                } else {
                    console.error("Booking error, redirecting anyway.");
                    window.location.href = "https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01";
                }
            } catch (err) {
                console.error("Network error, redirecting anyway.", err);
                window.location.href = "https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01";
            }
        }
"""
html = html.replace('</script>', script_js + '\n    </script>')

with open('index.html', 'w') as f:
    f.write(html)

print("Applied Progressive Disclosure and Multi-Step Booking successfully.")
