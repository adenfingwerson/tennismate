import re

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the style block for btn-brutalist-tab
style_pattern = re.compile(r'\.btn-brutalist-tab \{.*?\.btn-brutalist-tab\.active-accent \{.*?\}', re.DOTALL)

new_style = """\.btn-brutalist-tab {
            width: 100%; text-align: left; padding: 20px; 
            background: linear-gradient(135deg, #ccff00 0%, #aadd00 100%); 
            color: var(--text); 
            border: 3px solid var(--border-dark); font-size: 1.1rem; 
            font-weight: 900; text-transform: uppercase; letter-spacing: 1px;
            display: flex; justify-content: space-between; align-items: center; 
            cursor: pointer; transition: all 0.15s ease;
            box-shadow: 4px 4px 0px var(--border-dark);
        }
        .btn-brutalist-tab:hover {
            transform: translate(-2px, -2px);
            box-shadow: 6px 6px 0px var(--border-dark);
            background: linear-gradient(135deg, #d4ff33 0%, #b8e600 100%);
        }
        .btn-brutalist-tab.active {
            background: var(--text);
            color: var(--accent);
            box-shadow: 2px 2px 0px var(--border-dark);
            transform: translate(2px, 2px);
        }"""

# Update the buttons grid structure
top_grid_pattern = re.compile(r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(250px, 1fr\)\); gap: 16px; padding: 32px; background: #fff; border-top: 4px solid var\(--border-dark\);">.*?</div>\s*</details>\s*</div>\s*<!-- TAB 1', re.DOTALL)

top_grid_replacement = """<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; padding: 32px; background: #fff; border-top: 4px solid var(--border-dark);">
                
                <button class="btn-brutalist-tab tab-btn active" onclick="switchTab('tab-stats')">
                    <span>👤 Player Profile</span>
                    <span>→</span>
                </button>
                
                <button class="btn-brutalist-tab tab-btn" onclick="switchTab('tab-lessons')">
                    <span>📓 Training Journal</span>
                    <span>→</span>
                </button>

                <button class="btn-brutalist-tab tab-btn" style="position: relative; overflow: hidden;" onclick="switchTab('tab-tools')">
                    <span style="position: absolute; top: -10px; left: -10px; width: 24px; height: 24px; background: var(--text);"></span>
                    <span style="margin-left: 16px;">⚡ RaQGeN PRO</span>
                    <span>→</span>
                </button>

                <button class="btn-brutalist-tab" onclick="window.location.href='/'">
                    <span>📅 Book a Lesson</span>
                    <span>→</span>
                </button>

            </div>
        </details>
    </div>

    <!-- TAB 1"""

bottom_grid_pattern = re.compile(r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(250px, 1fr\)\); gap: 16px; padding: 32px; background: #fff; border-top: 4px solid var\(--border-dark\);">.*?</div>\s*</details>\s*</div>\s*</div>\s*<script>', re.DOTALL)

bottom_grid_replacement = """<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; padding: 32px; background: #fff; border-top: 4px solid var(--border-dark);">
                <button class="btn-brutalist-tab tab-btn active" onclick="switchTab('tab-stats'); window.scrollTo(0, 0);">
                    <span>👤 Player Profile</span>
                    <span>→</span>
                </button>
                <button class="btn-brutalist-tab tab-btn" onclick="switchTab('tab-lessons'); window.scrollTo(0, 0);">
                    <span>📓 Training Journal</span>
                    <span>→</span>
                </button>
                <button class="btn-brutalist-tab tab-btn" style="position: relative; overflow: hidden;" onclick="switchTab('tab-tools'); window.scrollTo(0, 0);">
                    <span style="position: absolute; top: -10px; left: -10px; width: 24px; height: 24px; background: var(--text);"></span>
                    <span style="margin-left: 16px;">⚡ RaQGeN PRO</span>
                    <span>→</span>
                </button>
                <button class="btn-brutalist-tab" onclick="window.location.href='/'">
                    <span>📅 Book a Lesson</span>
                    <span>→</span>
                </button>
            </div>
        </details>
    </div>

</div>
<script>"""

content = style_pattern.sub(new_style, content)
content = top_grid_pattern.sub(top_grid_replacement, content)
content = bottom_grid_pattern.sub(bottom_grid_replacement, content)

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated menu styling and buttons")
