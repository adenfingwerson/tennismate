import re

with open('profile.html', 'r') as f:
    html = f.read()

# CSS for the new AI cards
css_to_add = """
        /* AI Insight Modules (Hyper-Simple) */
        .ai-module {
            background: #111;
            border: 1px solid var(--border-dark);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            transition: transform 0.2s;
            cursor: default;
        }
        .ai-module:hover {
            transform: translateX(4px);
        }
        .ai-module-title {
            color: var(--accent);
            font-size: 0.8rem;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }
        .ai-module-content {
            color: #fff;
            font-size: 1.25rem;
            font-weight: 500;
            line-height: 1.4;
        }
        .ai-module-list {
            margin-top: 8px;
            padding-left: 20px;
            color: #ddd;
        }
        .ai-module-list li {
            margin-bottom: 8px;
            font-size: 1.1rem;
        }
"""
html = html.replace('</style>', css_to_add + '\n    </style>')

# Replace old gated content structure
old_gated_content = re.search(r'<div id="gated-content" class="gated-blur">.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
new_gated_content = """
            <!-- THE BLURRED CONTENT (AI Insights UI) -->
            <div id="gated-content" class="gated-blur">
                <div class="tactical-card" style="background: var(--bg); padding: 0;">
                    <div style="padding: 24px; border-bottom: 1px solid var(--border);">
                        <h3>Your Tactical Blueprint</h3>
                        <p style="color: var(--text-muted);">AI-generated strategy based on your latest coaching notes.</p>
                    </div>
                    
                    <div style="padding: 24px;">
                        <!-- Module 1 -->
                        <div class="ai-module">
                            <span class="ai-module-title">01 / The Big Goal</span>
                            <div class="ai-module-content" id="ai-focus">[Awaiting Analysis]</div>
                        </div>

                        <!-- Module 2 -->
                        <div class="ai-module">
                            <span class="ai-module-title">02 / Mechanical Cues</span>
                            <ul class="ai-module-list" id="ai-cues">
                                <li>[Awaiting Analysis]</li>
                            </ul>
                        </div>

                        <!-- Module 3 -->
                        <div class="ai-module">
                            <span class="ai-module-title">03 / The Golden Rule</span>
                            <div class="ai-module-content" id="ai-rule" style="font-weight: 900;">[Awaiting Analysis]</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""

if old_gated_content:
    html = html.replace(old_gated_content.group(0), new_gated_content)

# Update Javascript to bind to new IDs
js_to_replace = """
                if (metrics.ai_a_game) document.getElementById('ai-a-game').value = metrics.ai_a_game;
                if (metrics.ai_vuln) document.getElementById('ai-vuln').value = metrics.ai_vuln;
                if (metrics.ai_reset) document.getElementById('ai-reset').value = metrics.ai_reset;
"""
new_js = """
                if (metrics.ai_focus) document.getElementById('ai-focus').innerText = metrics.ai_focus;
                if (metrics.ai_rule) document.getElementById('ai-rule').innerText = metrics.ai_rule;
                if (metrics.ai_cues && Array.isArray(metrics.ai_cues)) {
                    const cuesList = document.getElementById('ai-cues');
                    cuesList.innerHTML = '';
                    metrics.ai_cues.forEach(cue => {
                        const li = document.createElement('li');
                        li.innerText = cue;
                        cuesList.appendChild(li);
                    });
                }
"""
html = html.replace(js_to_replace, new_js)

with open('profile.html', 'w') as f:
    f.write(html)
print("Profile UI updated")
