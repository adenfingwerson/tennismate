import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Replace Stripe links with Cal.com links
content = content.replace('https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01', 'https://cal.com/tennis-t-mate-hcmfls')
content = content.replace('Book Again', 'Book Session')

# 2. Extract sections
def extract_section(name):
    match = re.search(r'(<section class="'+name+r'".*?</section>)', content, re.DOTALL)
    if match:
        return match.group(1)
    return ""

hero = extract_section('hero')
roster = extract_section('roster')
logistics = extract_section('logistics')
testimonials = extract_section('testimonials')
second_cta = extract_section('second-cta')

packages = """
    <section class="packages">
        <div class="container grid">
            <div class="section-title">
                <span class="kicker">Pricing</span>
                <h2>Packages</h2>
            </div>
            <div class="section-content location-grid">
                <div class="location-card">
                    <h3>Single Lesson</h3>
                    <p style="font-size: 2rem; font-weight: 900; margin-bottom: 1rem;">$25</p>
                    <p style="color: var(--text-muted); margin-bottom: 2rem;">1 Hour Session</p>
                    <a href="https://cal.com/tennis-t-mate-hcmfls" class="btn" style="width: 100%; text-align: center;">Book Now</a>
                </div>
                <div class="location-card" style="background-color: var(--text); color: var(--bg);">
                    <h3>4-Lesson Pack</h3>
                    <p style="font-size: 2rem; font-weight: 900; margin-bottom: 1rem;">$90</p>
                    <p style="color: #aaa; margin-bottom: 2rem;">Save $10. Must be used within 6 weeks.</p>
                    <a href="https://cal.com/tennis-t-mate-hcmfls" class="btn" style="width: 100%; text-align: center; background-color: var(--bg); color: var(--text); border-color: var(--bg);">Book Pack</a>
                </div>
            </div>
        </div>
    </section>
"""

# Re-assemble the body
body_start = content.split('<section class="hero">')[0]
footer = content.split('<footer>')[1]

new_body = (
    body_start +
    hero + "\n" +
    roster + "\n" +
    packages + "\n" +
    logistics + "\n" +
    testimonials + "\n" +
    second_cta + "\n" +
    "    <footer>" + footer
)

with open('index.html', 'w') as f:
    f.write(new_body)

