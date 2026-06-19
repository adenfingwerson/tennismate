import re

def update_profile():
    with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the bottom accordion
    content = re.sub(r'<!-- BOTTOM TM8 T00LS EXPANDABLE SECTION -->.*?</div>\s*</details>\s*</div>', '', content, flags=re.DOTALL)
    
    # 2. Replace the top accordion with standard, clean tabs
    tabs_html = """<!-- TABS NAVIGATION -->
    <div class="tabs">
        <button class="tab-btn active" onclick="switchTab('tab-stats')">Player Profile</button>
        <button class="tab-btn" onclick="switchTab('tab-lessons')">Coaching Notes</button>
        <button class="tab-btn" onclick="switchTab('tab-tools')">RaQGeN Engine</button>
    </div>"""
    content = re.sub(r'<!-- TM8 T00LS EXPANDABLE SECTION -->.*?</div>\s*</details>\s*</div>', tabs_html, content, flags=re.DOTALL)

    # 3. Replace the overly complex SVG logo with the "whispering" elegant text logo
    logo_pattern = re.compile(r'<!-- 2026 Academic / Brutalist Logo -->.*?</div>', re.DOTALL)
    elegant_logo_light = """<!-- Elegant Whispering Logo -->
                <div style="display: inline-block; margin-bottom: 8px;">
                    <span style="font-family: 'Inter', sans-serif; font-weight: 300; font-size: 1.1rem; letter-spacing: 8px; text-transform: uppercase; color: #555;">RaQGeN</span>
                </div>"""
    content = logo_pattern.sub(elegant_logo_light, content, count=1)

    # 4. Add a tiny script to check for incoming tab links
    tab_script = """
    // Check if we came from the homepage menu
    window.addEventListener('DOMContentLoaded', () => {
        const urlParams = new URLSearchParams(window.location.search);
        const openTab = urlParams.get('tab');
        if (openTab) {
            switchTab('tab-' + openTab);
        }
    });
    """
    content = content.replace('// Tab switching logic', tab_script + '\n    // Tab switching logic')

    with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'w', encoding='utf-8') as f:
        f.write(content)

def update_index():
    with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert TM8 T00LS right after the hero section
    menu_html = """
    <!-- TM8 T00LS EXPANDABLE SECTION -->
    <div class="container" style="position: relative; z-index: 10; margin-top: -30px; margin-bottom: 60px; max-width: 1000px;">
        <style>
            @keyframes subtlePulse {
                0% { transform: scale(1); opacity: 1; }
                50% { transform: scale(1.2); opacity: 0.8; }
                100% { transform: scale(1); opacity: 1; }
            }
            .master-accordion {
                background: #fff; border: 4px solid var(--border-dark); 
                box-shadow: 8px 8px 0px var(--border-dark); 
                transition: transform 0.15s ease, box-shadow 0.15s ease;
            }
            .master-accordion:hover {
                transform: translate(-4px, -4px);
                box-shadow: 12px 12px 0px var(--border-dark);
            }
            .master-summary {
                padding: 20px 30px; font-size: 1.2rem; font-weight: 900; 
                cursor: pointer; list-style: none; display: flex; 
                justify-content: space-between; align-items: center; 
                color: var(--text); text-transform: uppercase; letter-spacing: 1px;
            }
            .master-summary::-webkit-details-marker { display: none; }
            .pulse-dot {
                display: inline-block; width: 12px; height: 12px; 
                background: var(--accent); border: 2px solid var(--text); 
                border-radius: 50%; animation: subtlePulse 2s infinite;
            }
            .tm8-link {
                text-decoration: none; color: #000; padding: 20px 30px; 
                font-weight: 800; text-transform: uppercase; letter-spacing: 1px; 
                display: flex; justify-content: space-between; align-items: center; 
                transition: background 0.2s, padding-left 0.2s;
                border-bottom: 2px solid #eee;
                font-size: 0.95rem;
            }
            .tm8-link:hover {
                background: #f9f9f9; padding-left: 35px;
            }
            .tm8-link.accent {
                background: linear-gradient(135deg, #ccff00 0%, #aadd00 100%);
                border-bottom: none;
            }
            .tm8-link.accent:hover {
                background: linear-gradient(135deg, #d4ff33 0%, #b8e600 100%);
            }
        </style>
        <div class="master-accordion">
            <details style="padding: 0;">
                <summary class="master-summary">
                    <span style="display: flex; align-items: center; gap: 12px;">
                        <span class="pulse-dot"></span>
                        TM8 T00LS
                    </span>
                    <span style="font-size: 1.4rem; font-weight: 400;">+</span>
                </summary>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); border-top: 4px solid var(--border-dark); background: #fff;">
                    <a href="/profile.html?tab=stats" class="tm8-link" style="border-right: 2px solid #eee;">
                        Player Profile <span>&rarr;</span>
                    </a>
                    <a href="/profile.html?tab=lessons" class="tm8-link" style="border-right: 2px solid #eee;">
                        Coaching Notes <span>&rarr;</span>
                    </a>
                    <a href="/blog" class="tm8-link" style="border-right: 2px solid #eee;">
                        The Journal <span>&rarr;</span>
                    </a>
                    <a href="#raqgen" class="tm8-link" style="border-right: 2px solid #eee;" onclick="document.querySelector('.raqgen-section').scrollIntoView({behavior: 'smooth'}); return false;">
                        RaQGeN Engine <span>&rarr;</span>
                    </a>
                    <a href="#" onclick="openModal(event)" class="tm8-link accent">
                        Book a Lesson <span>&rarr;</span>
                    </a>
                </div>
            </details>
        </div>
    </div>
"""
    # Insert right after the hero section
    content = content.replace('</section>\n\n    <section class="details-accordion"', '</section>\n' + menu_html + '\n    <section class="details-accordion"')

    # 2. Replace the overly complex SVG logo with the "whispering" elegant text logo
    logo_pattern = re.compile(r'<!-- 2026 Academic / Brutalist Logo -->.*?</div>', re.DOTALL)
    elegant_logo_dark = """<!-- Elegant Whispering Logo -->
                <div style="display: inline-block; margin-bottom: 16px;">
                    <span style="font-family: 'Inter', sans-serif; font-weight: 300; font-size: 1.1rem; letter-spacing: 12px; text-transform: uppercase; color: #888;">RaQGeN</span>
                </div>"""
    content = logo_pattern.sub(elegant_logo_dark, content, count=1)

    # 3. Add an id="raqgen" to the raqgen section so the anchor link works
    content = content.replace('<section class="raqgen-section"', '<section id="raqgen" class="raqgen-section"')

    with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', 'w', encoding='utf-8') as f:
        f.write(content)

update_profile()
update_index()
print("Updated files successfully.")
