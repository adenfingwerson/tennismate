import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace the bulky 3 sections (roster, packages, logistics) with one unified "details" grid that uses Progressive Disclosure/Chunking
old_sections = re.search(r'<section class="roster">.*?</section>\s*<section class="packages">.*?</section>\s*<section class="logistics">.*?</section>', html, re.DOTALL)

new_section = """
    <section class="logistics-unified" style="padding: 80px 0;">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px;">
                
                <!-- Coach Chunk -->
                <div style="border: 1px solid var(--border-dark); padding: 32px; border-radius: 8px;">
                    <span class="kicker">The Coach</span>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Aden Ingwerson</h3>
                    <p style="color: var(--text-muted); font-size: 1.1rem;">Collegiate player focused on modern stroke mechanics and solid fundamentals for all skill levels.</p>
                </div>

                <!-- Pricing Chunk -->
                <div style="border: 1px solid var(--border-dark); padding: 32px; border-radius: 8px; background: var(--bg); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <span class="kicker">The Rate</span>
                        <h3 style="font-size: 2.5rem; margin-bottom: 0.5rem; line-height: 1;">$25<span style="font-size: 1.1rem; color: var(--text-muted); font-weight: 500;">/hour</span></h3>
                        <p style="color: var(--text-muted); font-size: 1.1rem; margin-bottom: 2rem;">No hidden fees. No commitments. Just show up and hit.</p>
                    </div>
                    <a href="https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01" class="btn" style="text-align: center; width: 100%;">Book Session</a>
                </div>

                <!-- Locations Chunk -->
                <div style="border: 1px solid var(--border-dark); padding: 32px; border-radius: 8px;">
                    <span class="kicker">The Locations</span>
                    <div style="margin-bottom: 1.5rem;">
                        <h4 style="font-size: 1.2rem; margin-bottom: 0.25rem;">Holdrege, NE</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Mon - Sun • North Park Courts</p>
                    </div>
                    <div>
                        <h4 style="font-size: 1.2rem; margin-bottom: 0.25rem;">Hastings, NE</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Thursdays • Hastings College</p>
                    </div>
                </div>

            </div>
        </div>
    </section>
"""

if old_sections:
    html = html.replace(old_sections.group(0), new_section)
    with open('index.html', 'w') as f:
        f.write(html)
    print("Updated successfully")
else:
    print("Could not find sections to replace")
