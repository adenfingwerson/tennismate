import re

with open('/tmp/scripts.html', 'r') as f:
    scripts_content = f.read()

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Tennis T-Mate — Experimental</title>
    <link rel="canonical" href="https://tennistmate.com/">
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#ECD06F">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --black: #000000;
            --white: #ffffff;
            --yellow: #ECD06F;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            cursor: none; /* Custom cursor */
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--white);
            color: var(--black);
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* CUSTOM CURSOR */
        #cursor {
            position: fixed;
            top: 0; left: 0;
            width: 20px; height: 20px;
            background-color: var(--yellow);
            border-radius: 50%;
            pointer-events: none;
            mix-blend-mode: difference;
            z-index: 10000;
            transition: transform 0.1s ease;
        }
        .hover-target:hover ~ #cursor,
        a:hover ~ #cursor,
        button:hover ~ #cursor {
            transform: scale(3);
        }

        h1, h2, h3, .display-text {
            font-family: 'Syne', sans-serif;
            text-transform: uppercase;
            line-height: 0.9;
        }

        a, button {
            cursor: none;
        }

        /* NAVBAR */
        nav {
            position: fixed;
            top: 0; width: 100%;
            padding: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 100;
            mix-blend-mode: difference;
            color: var(--white);
        }
        .nav-logo {
            font-family: 'Syne', sans-serif;
            font-size: 1.5rem;
            font-weight: 800;
        }
        #admin-link {
            font-weight: 700;
            border: 2px solid var(--white);
            padding: 8px 16px;
            border-radius: 50px;
            text-decoration: none;
            color: var(--white);
        }

        /* HERO SECTION */
        .hero {
            height: 100vh;
            background-color: var(--black);
            color: var(--white);
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 24px;
            position: relative;
            overflow: hidden;
        }
        .hero h1 {
            font-size: clamp(4rem, 15vw, 12rem);
            margin-bottom: 24px;
            position: relative;
            z-index: 2;
        }
        .hero h1 span {
            color: var(--yellow);
        }
        .hero p {
            font-size: clamp(1.2rem, 3vw, 2rem);
            max-width: 600px;
            z-index: 2;
        }
        
        .btn-huge {
            display: inline-block;
            background-color: var(--yellow);
            color: var(--black);
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: clamp(2rem, 5vw, 4rem);
            padding: 24px 48px;
            border-radius: 100px;
            border: none;
            margin-top: 48px;
            text-decoration: none;
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            align-self: flex-start;
        }
        .btn-huge:hover {
            transform: scale(1.05);
        }

        /* MARQUEE */
        .marquee {
            background: var(--yellow);
            color: var(--black);
            padding: 24px 0;
            white-space: nowrap;
            overflow: hidden;
            border-top: 4px solid var(--black);
            border-bottom: 4px solid var(--black);
        }
        .marquee-inner {
            display: inline-block;
            animation: marquee 15s linear infinite;
            font-family: 'Syne', sans-serif;
            font-size: 3rem;
            font-weight: 800;
            text-transform: uppercase;
        }
        @keyframes marquee {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }

        /* SECTIONS */
        .section-padding {
            padding: 120px 24px;
        }
        .bg-white { background: var(--white); color: var(--black); }
        .bg-black { background: var(--black); color: var(--white); }
        .bg-yellow { background: var(--yellow); color: var(--black); }

        /* ACCORDION (Repainted) */
        .accordion-item {
            border-bottom: 4px solid var(--black);
        }
        .accordion-item:first-child {
            border-top: 4px solid var(--black);
        }
        .accordion-header {
            width: 100%;
            text-align: left;
            background: none;
            border: none;
            font-family: 'Syne', sans-serif;
            font-size: clamp(2rem, 6vw, 4rem);
            font-weight: 800;
            padding: 40px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .accordion-icon {
            font-size: 4rem;
            font-weight: 400;
            transition: transform 0.4s ease;
        }
        .accordion-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .accordion-item.active .accordion-content {
            max-height: 1000px;
        }
        .accordion-item.active .accordion-icon {
            transform: rotate(45deg);
        }
        .accordion-inner {
            padding-bottom: 40px;
            font-size: 1.25rem;
        }

        /* GRID/CARDS */
        .roster-grid {
            display: flex;
            gap: 24px;
            flex-wrap: wrap;
        }
        .roster-card {
            flex: 1 1 300px;
            background: var(--yellow);
            border: 4px solid var(--black);
            border-radius: 24px;
            padding: 24px;
        }
        .roster-image {
            width: 100%;
            height: auto;
            border-radius: 12px;
            border: 4px solid var(--black);
            margin-bottom: 16px;
        }

        /* RAQGEN */
        .raqgen-section {
            border-top: 4px solid var(--black);
            border-bottom: 4px solid var(--black);
        }
        .tm-input, select {
            width: 100%;
            background: transparent;
            border: none;
            border-bottom: 4px solid var(--black);
            font-size: 2rem;
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            padding: 16px 0;
            margin-bottom: 32px;
            color: var(--black);
            outline: none;
            border-radius: 0;
            appearance: none;
        }
        .tm-input::placeholder { color: rgba(0,0,0,0.3); }
        .raqgen-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 60px;
        }

        /* BOTTOM SHEET MODAL (Phone First) */
        .modal-overlay {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100vh;
            background: rgba(0,0,0,0.8);
            z-index: 9999;
            display: none; /* toggled by JS */
            flex-direction: column;
            justify-content: flex-end;
        }
        .modal-content {
            background: var(--yellow);
            width: 100%;
            height: 90vh;
            border-radius: 40px 40px 0 0;
            padding: 40px 24px;
            position: relative;
            animation: slideUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            overflow-y: auto;
        }
        @keyframes slideUp {
            from { transform: translateY(100%); }
            to { transform: translateY(0); }
        }
        .modal-close {
            position: absolute;
            top: 24px; right: 24px;
            font-size: 3rem;
            font-weight: 300;
            line-height: 1;
        }
        
        .booking-step {
            display: none;
            animation: fadeIn 0.4s ease forwards;
        }
        .booking-step.active {
            display: block;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .modal-title {
            font-size: clamp(2.5rem, 8vw, 4rem);
            margin-bottom: 8px;
        }
        .modal-subtitle {
            font-size: 1.25rem;
            margin-bottom: 40px;
            font-weight: 500;
        }

        /* Radio Options */
        .radio-group {
            display: flex;
            flex-direction: column;
            gap: 16px;
            margin-bottom: 40px;
        }
        .radio-option {
            border: 4px solid var(--black);
            border-radius: 24px;
            padding: 24px;
            background: var(--white);
            transition: all 0.2s ease;
        }
        .radio-option.selected {
            background: var(--black);
            color: var(--white);
        }
        .radio-option-title {
            display: block;
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 2rem;
        }

        /* Modal Inputs */
        .booking-step input {
            background: var(--white);
            border: 4px solid var(--black);
            border-radius: 16px;
            padding: 20px;
            font-size: 1.5rem;
            font-weight: 600;
            width: 100%;
            margin-bottom: 24px;
            outline: none;
            font-family: 'Inter', sans-serif;
        }

        /* Step Dots */
        .step-indicator {
            display: flex;
            gap: 12px;
            margin-bottom: 40px;
        }
        .step-dot {
            width: 12px; height: 12px;
            border-radius: 50%;
            background: var(--black);
            opacity: 0.2;
        }
        .step-dot.active {
            opacity: 1;
        }

        .btn-modal {
            background: var(--black);
            color: var(--yellow);
            font-family: 'Syne', sans-serif;
            font-size: 1.5rem;
            font-weight: 800;
            padding: 20px 40px;
            border-radius: 100px;
            border: none;
            width: 100%;
            margin-bottom: 16px;
        }
        .btn-prev {
            background: transparent;
            color: var(--black);
            border: 4px solid var(--black);
        }

        /* Large Bar Graphs for RaQGeN */
        .bar-wrap {
            height: 60px;
            border: 4px solid var(--black);
            border-radius: 100px;
            overflow: hidden;
            margin-top: 8px;
            background: var(--white);
        }
        .bar-fill {
            height: 100%;
            background: var(--black);
            width: 0%;
            transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
    </style>
</head>
<body>
    <div id="cursor"></div>

    <nav>
        <div class="nav-logo">TENNIS T-MATE</div>
        <a href="/admin.html" id="admin-link">ADMIN</a>
    </nav>

    <!-- HERO -->
    <section class="hero hover-target">
        <h1>TENNIS<br>LESSONS IN<br><span>HASTINGS</span> &<br><span>HOLDREGE</span></h1>
        <p>Private coaching for kids, high school players, and adults. $25/hour.</p>
        <button class="btn-huge hover-target" onclick="openModal()">BOOK SESSION &rarr;</button>
    </section>

    <!-- MARQUEE -->
    <div class="marquee hover-target">
        <div class="marquee-inner">
            NO HIDDEN FEES &mdash; 1 HOUR SESSIONS &mdash; ALL SKILL LEVELS &mdash; NO HIDDEN FEES &mdash; 1 HOUR SESSIONS &mdash; ALL SKILL LEVELS &mdash; 
        </div>
    </div>

    <!-- ACCORDION / INFO -->
    <section class="bg-white section-padding hover-target">
        <h2 style="font-size: clamp(3rem, 10vw, 6rem); margin-bottom: 60px;">DETAILS.</h2>
        
        <div class="accordion-item" onclick="this.classList.toggle('active')">
            <button class="accordion-header">
                The Roster <span class="accordion-icon">+</span>
            </button>
            <div class="accordion-content">
                <div class="accordion-inner roster-grid">
                    <div class="roster-card">
                        <img src="assets/aden.jpg" alt="Aden Ingwerson" class="roster-image" onerror="this.style.display='none'">
                        <h3 style="font-size: 2rem; margin-bottom: 8px;">Aden Ingwerson</h3>
                        <p style="font-weight: 700; margin-bottom: 16px;">Coach (Holdrege & Hastings)</p>
                        <p>Current collegiate player focused on building solid fundamentals and modern stroke mechanics. Looking to coach all skill levels.</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="accordion-item" onclick="this.classList.toggle('active')">
            <button class="accordion-header">
                Pricing & Rates <span class="accordion-icon">+</span>
            </button>
            <div class="accordion-content">
                <div class="accordion-inner">
                    <h3 style="font-size: 3rem; margin-bottom: 16px;">$25 / Single Lesson</h3>
                    <p>1 Hour Session. No hidden fees. No commitments.</p>
                </div>
            </div>
        </div>

        <div class="accordion-item" onclick="this.classList.toggle('active')">
            <button class="accordion-header">
                Locations <span class="accordion-icon">+</span>
            </button>
            <div class="accordion-content">
                <div class="accordion-inner" style="display: flex; gap: 40px; flex-wrap: wrap;">
                    <div>
                        <h3 style="font-size: 2rem;">Holdrege, NE</h3>
                        <p>North Park Courts<br>Mon - Sun</p>
                    </div>
                    <div>
                        <h3 style="font-size: 2rem;">Hastings, NE</h3>
                        <p>Hastings College<br>Thursdays Only</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- RAQGEN SECTION -->
    <section id="raqgen" class="bg-yellow section-padding raqgen-section hover-target">
        <h2 style="font-size: clamp(3rem, 10vw, 6rem); margin-bottom: 24px; line-height: 0.9;">RAQGEN OS</h2>
        <p style="font-size: 1.5rem; font-weight: 500; margin-bottom: 80px; max-width: 800px;">
            Personalized Racket Recommendation Engine. Powered by TennisT-Mate's Equations, OSINT data, and the Mahalanobis Distance Model.
        </p>

        <div class="raqgen-grid">
            <div>
                <h3 style="font-size: 2rem; margin-bottom: 24px;">Biomechanics</h3>
                <label>Height (Inches)</label>
                <input type="number" id="idx-raq-height" placeholder="72" class="tm-input">
                
                <label>Weight (lbs)</label>
                <input type="number" id="idx-raq-weight" placeholder="165" class="tm-input">
                
                <label>Wingspan (Inches)</label>
                <input type="number" id="idx-raq-wingspan" placeholder="74" class="tm-input">
            </div>
            
            <div>
                <h3 style="font-size: 2rem; margin-bottom: 24px;">Dynamics</h3>
                <label>Forehand Grip</label>
                <select id="idx-raq-grip" class="tm-input">
                    <option>Eastern</option>
                    <option selected>Semi-Western</option>
                    <option>Western</option>
                </select>

                <label>Backhand</label>
                <select id="idx-raq-bh" class="tm-input">
                    <option>One-Handed</option>
                    <option selected>Two-Handed</option>
                </select>

                <label>Playing Style</label>
                <select id="idx-raq-style" class="tm-input">
                    <option>Aggressive Baseliner</option>
                    <option selected>All-Court Player</option>
                    <option>Counter-Puncher</option>
                    <option>Serve & Volley</option>
                </select>
            </div>
        </div>

        <button id="btn-idx-raqgen" class="btn-huge hover-target" style="background: var(--black); color: var(--yellow); width: 100%; margin-top: 60px;" onclick="runIndexRaqGen()">RECALCULATE OPTIMIZATION</button>

        <!-- RESULTS -->
        <div id="idx-raqgen-result" style="display: none; margin-top: 80px; border-top: 4px solid var(--black); padding-top: 80px;">
            <div style="background: var(--black); color: var(--white); padding: 40px; border-radius: 40px; margin-bottom: 40px;">
                <h3 style="color: var(--yellow); margin-bottom: 16px;">BEST MATCH <span id="idx-raqgen-score" style="float:right;">100%</span></h3>
                <h4 id="idx-raqgen-name" style="font-size: clamp(2rem, 6vw, 4rem); margin-bottom: 40px;">--</h4>

                <div style="margin-bottom: 24px;">
                    <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.2rem;">
                        <span>Biomechanics Match</span>
                        <span id="idx-bar-bio-val">--%</span>
                    </div>
                    <div class="bar-wrap">
                        <div id="idx-bar-bio" class="bar-fill" style="background: var(--yellow);"></div>
                    </div>
                </div>

                <div style="margin-bottom: 24px;">
                    <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.2rem;">
                        <span>Tactical Match</span>
                        <span id="idx-bar-tac-val">--%</span>
                    </div>
                    <div class="bar-wrap">
                        <div id="idx-bar-tac" class="bar-fill" style="background: var(--yellow);"></div>
                    </div>
                </div>

                <div style="margin-bottom: 40px;">
                    <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.2rem;">
                        <span>Safety Factor</span>
                        <span id="idx-bar-safe-val">--%</span>
                    </div>
                    <div class="bar-wrap">
                        <div id="idx-bar-safe" class="bar-fill" style="background: #fff;"></div>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
                    <div><span style="color: #888;">Mass</span> <br><span id="idx-raqgen-weight" style="font-size: 2rem; font-weight: 800;">--</span></div>
                    <div><span style="color: #888;">Swingweight</span> <br><span id="idx-raqgen-sw" style="font-size: 2rem; font-weight: 800;">--</span></div>
                    <div><span style="color: #888;">Stiffness (RA)</span> <br><span id="idx-raqgen-ra" style="font-size: 2rem; font-weight: 800;">--</span></div>
                    <div><span style="color: #888;">Pattern</span> <br><span id="idx-raqgen-pattern" style="font-size: 2rem; font-weight: 800;">--</span></div>
                </div>
            </div>

            <!-- HIDDEN TW METRICS (kept to prevent JS errors, but stylized nicely if wanted, let's just hide them in a details tag) -->
            <details style="margin-bottom: 40px;">
                <summary style="font-family: 'Syne'; font-size: 1.5rem; font-weight: 700; cursor: none;">View TW Playtest Metrics</summary>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 24px; font-weight: 700;">
                    <div>Overall: <span id="idx-tw-overall">--</span></div>
                    <div>Power: <span id="idx-tw-power">--</span></div>
                    <div>Control: <span id="idx-tw-control">--</span></div>
                    <div>Maneuver: <span id="idx-tw-maneuver">--</span></div>
                    <div>Stability: <span id="idx-tw-stability">--</span></div>
                    <div>Comfort: <span id="idx-tw-comfort">--</span></div>
                    <div>Topspin: <span id="idx-tw-topspin">--</span></div>
                    <div>Touch: <span id="idx-tw-touch">--</span></div>
                    <div>Ground: <span id="idx-tw-ground">--</span></div>
                    <div>Volleys: <span id="idx-tw-volleys">--</span></div>
                    <div>Serves: <span id="idx-tw-serves">--</span></div>
                    <div>Returns: <span id="idx-tw-returns">--</span></div>
                </div>
            </details>

            <h3 style="font-size: 2rem; margin-bottom: 16px;">RUNNERS UP</h3>
            <div style="background: var(--white); border: 4px solid var(--black); padding: 24px; border-radius: 24px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center;">
                <span id="idx-ru1-name" style="font-family: 'Syne'; font-size: 1.5rem; font-weight: 800;">--</span>
                <span id="idx-ru1-score" style="background: var(--black); color: var(--white); padding: 8px 16px; border-radius: 100px; font-weight: 800;">--%</span>
            </div>
            <div style="background: var(--white); border: 4px solid var(--black); padding: 24px; border-radius: 24px; display: flex; justify-content: space-between; align-items: center;">
                <span id="idx-ru2-name" style="font-family: 'Syne'; font-size: 1.5rem; font-weight: 800;">--</span>
                <span id="idx-ru2-score" style="background: var(--black); color: var(--white); padding: 8px 16px; border-radius: 100px; font-weight: 800;">--%</span>
            </div>

        </div>
    </section>

    <!-- FOOTER CTA -->
    <section class="bg-black section-padding hover-target" style="text-align: center;">
        <h2 style="font-size: clamp(3rem, 12vw, 8rem); margin-bottom: 40px;">READY TO HIT?</h2>
        <button class="btn-huge hover-target" style="margin-top: 0;" onclick="openModal()">BOOK SESSION</button>
        
        <div style="margin-top: 120px;">
            <h3 style="font-size: 2rem; margin-bottom: 16px;">INQUIRIES</h3>
            <a href="tel:3089910173" class="hover-target" style="font-size: 2rem; font-weight: 700; color: var(--yellow); text-decoration: underline;">(308) 991-0173</a>
        </div>
    </section>

    <!-- BOOKING MODAL (BOTTOM SHEET) -->
    <div class="modal-overlay" id="bookingModal">
        <div class="modal-content">
            <div class="modal-close hover-target" onclick="closeModal()">&times;</div>
            
            <div class="step-indicator">
                <div class="step-dot active" id="dot-1"></div>
                <div class="step-dot" id="dot-2"></div>
                <div class="step-dot" id="dot-3"></div>
            </div>

            <form id="bookingForm" onsubmit="submitBooking(event)">
                
                <!-- STEP 1 -->
                <div class="booking-step active" id="step-1">
                    <h2 class="modal-title">Where?</h2>
                    <p class="modal-subtitle">Select a location to continue.</p>
                    
                    <div class="radio-group">
                        <div class="radio-option selected hover-target" onclick="selectRadio('location', 'Holdrege', this)">
                            <span class="radio-option-title">Holdrege, NE</span>
                            <span class="radio-option-desc">North Park Courts • Mon - Sun</span>
                        </div>
                        <div class="radio-option hover-target" onclick="selectRadio('location', 'Hastings', this)">
                            <span class="radio-option-title">Hastings, NE</span>
                            <span class="radio-option-desc">Hastings College • Thursdays Only</span>
                        </div>
                    </div>
                    <input type="hidden" id="b_location" value="Holdrege">
                    
                    <button type="button" class="btn-modal btn-next hover-target" onclick="nextStep(2)">Continue &rarr;</button>
                </div>

                <!-- STEP 2 -->
                <div class="booking-step" id="step-2">
                    <h2 class="modal-title">When?</h2>
                    <p class="modal-subtitle">Propose a day and time. We'll finalize via text.</p>
                    
                    <label style="font-weight: 700; font-size: 1.2rem; display: block; margin-bottom: 8px;">Preferred Day & Time</label>
                    <input type="text" id="b_time" class="hover-target" placeholder="e.g., Tuesday at 4:30 PM" required>
                    
                    <button type="button" class="btn-modal btn-next hover-target" onclick="nextStep(3)">Continue &rarr;</button>
                    <button type="button" class="btn-modal btn-prev hover-target" onclick="nextStep(1)">&larr; Back</button>
                </div>

                <!-- STEP 3 -->
                <div class="booking-step" id="step-3">
                    <h2 class="modal-title">Final Details</h2>
                    <p class="modal-subtitle">We'll redirect you to Stripe to lock in the $25.</p>
                    
                    <label style="font-weight: 700; font-size: 1.2rem; display: block; margin-bottom: 8px;">Full Name</label>
                    <input type="text" id="b_name" class="hover-target" placeholder="John Doe" required>
                    
                    <label style="font-weight: 700; font-size: 1.2rem; display: block; margin-bottom: 8px;">Phone Number</label>
                    <input type="tel" id="b_phone" class="hover-target" placeholder="(555) 123-4567" required>
                    
                    <button type="submit" class="btn-modal btn-submit hover-target" id="b_submit" style="background: var(--yellow); color: var(--black);">Pay $25 on Stripe &rarr;</button>
                    <button type="button" class="btn-modal btn-prev hover-target" onclick="nextStep(2)">&larr; Back</button>
                </div>
            </form>
        </div>
    </div>

    <!-- CUSTOM CURSOR JS -->
    <script>
        const cursor = document.getElementById('cursor');
        document.addEventListener('mousemove', e => {
            cursor.style.left = e.clientX - 10 + 'px';
            cursor.style.top = e.clientY - 10 + 'px';
        });
    </script>

"""

with open('/tmp/new_index.html', 'w') as f:
    f.write(html_content + "\n" + scripts_content + "\n</body>\n</html>")

