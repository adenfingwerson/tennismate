import re

with open('index.html', 'r') as f:
    content = f.read()

philosophy_html = """
    <section class="philosophy" style="padding: 120px 0; border-bottom: 1px solid var(--border-dark);">
        <div class="container grid">
            <div class="section-title">
                <span class="kicker">The Approach</span>
                <h2>Why Train Here?</h2>
            </div>
            <div class="section-content" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 3rem;">
                <div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">No Fluff, Just Reps.</h3>
                    <p style="color: var(--text-muted);">We skip the country-club talk and focus strictly on what works in real matches. Modern swing paths, heavy spin, and footwork that actually holds up under pressure.</p>
                </div>
                <div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">College-Level Intensity.</h3>
                    <p style="color: var(--text-muted);">You're hitting with an active collegiate player. The pacing, the drills, and the feedback are pulled directly from college practices. It's about building a weaponized game.</p>
                </div>
            </div>
        </div>
    </section>
"""

# Insert after the packages section
new_content = re.sub(r'(<section class="packages">.*?</section>)', r'\1\n' + philosophy_html, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(new_content)
