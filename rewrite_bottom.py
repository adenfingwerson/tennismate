import re

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'r', encoding='utf-8') as f:
    content = f.read()

# First, there's a rogue neon button at the bottom of profile.html.
# We'll remove it, then inject a duplicate of the master-accordion right before the end of the container.
content = re.sub(r'<button class="tm-btn" id="btn-raqgen"[^>]+>.*?INITIALIZE MASTER EQUATION.*?</button>', '', content, flags=re.DOTALL)

# Let's insert the master-accordion at the end of the container.
bottom_menu = """
    <!-- BOTTOM TM8 T00LS EXPANDABLE SECTION -->
    <div class="master-accordion">
        <details style="padding: 0;">
            <summary class="master-summary">
                <span style="display: flex; align-items: center; gap: 16px;">
                    <span class="pulse-dot"></span>
                    TM8 T00LS
                </span>
                <span style="font-size: 0.9rem; font-weight: 900; background: var(--text); color: var(--bg); padding: 8px 16px; letter-spacing: 1px; display: flex; align-items: center; gap: 8px;">
                    OPEN WORKSPACE <span style="font-size: 1.4rem; line-height: 0;">+</span>
                </span>
            </summary>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; padding: 32px; background: #fff; border-top: 4px solid var(--border-dark);">
                <button class="btn-brutalist-tab tab-btn active" onclick="switchTab('tab-stats'); window.scrollTo(0, 0);">
                    <span>Player Profile</span>
                    <span>→</span>
                </button>
                <button class="btn-brutalist-tab tab-btn" onclick="switchTab('tab-lessons'); window.scrollTo(0, 0);">
                    <span>Training Journal</span>
                    <span>→</span>
                </button>
                <button class="btn-brutalist-tab tab-btn" style="position: relative; overflow: hidden;" onclick="switchTab('tab-tools'); window.scrollTo(0, 0);">
                    <span style="position: absolute; top: -10px; left: -10px; width: 24px; height: 24px; background: var(--text);"></span>
                    <span style="margin-left: 16px;">RaQGeN OS V.2</span>
                    <span>→</span>
                </button>
            </div>
        </details>
    </div>
"""

# The main container closes around here:
# </div>
# </div>
# <script>
# We replace the last two closing divs before the script tags.
container_close_pattern = re.compile(r'</div>\s*</div>\s*<script>', re.DOTALL)
new_container_close = f"</div>\n{bottom_menu}\n</div>\n<script>"

content = container_close_pattern.sub(new_container_close, content, count=1)

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected bottom menu.")
