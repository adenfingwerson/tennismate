import re

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<!-- TM8 T00LS EXPANDABLE SECTION -->.*?</details>\s*</div>', re.DOTALL)

new_section = """<!-- TM8 T00LS EXPANDABLE SECTION -->
    <style>
        @keyframes subtlePulse {
            0% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.2); opacity: 0.8; }
            100% { transform: scale(1); opacity: 1; }
        }
        .master-accordion {
            width: 100%; max-width: 1000px; margin: 0 auto 40px auto; 
            background: #fff; border: 4px solid var(--border-dark); 
            box-shadow: 8px 8px 0px var(--border-dark); 
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }
        .master-accordion:hover {
            transform: translate(-4px, -4px);
            box-shadow: 12px 12px 0px var(--border-dark);
        }
        .master-summary {
            padding: 24px 32px; font-size: 1.5rem; font-weight: 900; 
            cursor: pointer; list-style: none; display: flex; 
            justify-content: space-between; align-items: center; 
            color: var(--text); text-transform: uppercase; letter-spacing: -0.02em;
        }
        .master-summary::-webkit-details-marker { display: none; }
        
        .pulse-dot {
            display: inline-block; width: 14px; height: 14px; 
            background: var(--accent); border: 3px solid var(--text); 
            border-radius: 50%; animation: subtlePulse 2s infinite;
        }
        .btn-brutalist-tab {
            width: 100%; text-align: left; padding: 20px; 
            background: #f4f4f4; color: var(--text); 
            border: 3px solid var(--border-dark); font-size: 1.1rem; 
            font-weight: 900; text-transform: uppercase; letter-spacing: 1px;
            display: flex; justify-content: space-between; align-items: center; 
            cursor: pointer; transition: all 0.1s ease;
        }
        .btn-brutalist-tab:hover {
            background: #e5e5e5;
        }
        .btn-brutalist-tab.active {
            background: var(--text);
            color: var(--bg);
        }
        .btn-brutalist-tab.active-accent {
            background: var(--accent);
            color: var(--text);
        }
    </style>
    
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
                
                <button class="btn-brutalist-tab tab-btn active" onclick="switchTab('tab-stats')">
                    <span>Player Profile</span>
                    <span>→</span>
                </button>
                
                <button class="btn-brutalist-tab tab-btn" onclick="switchTab('tab-lessons')">
                    <span>Training Journal</span>
                    <span>→</span>
                </button>

                <button class="btn-brutalist-tab tab-btn" style="position: relative; overflow: hidden;" onclick="switchTab('tab-tools')">
                    <span style="position: absolute; top: -10px; left: -10px; width: 24px; height: 24px; background: var(--text);"></span>
                    <span style="margin-left: 16px;">RaQGeN OS V.2</span>
                    <span>→</span>
                </button>

            </div>
        </details>
    </div>"""

content = pattern.sub(new_section, content, count=1)

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Menu update complete")
