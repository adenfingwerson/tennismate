import re

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. REMOVE the old TM8 T00LS EXPANDABLE SECTION and the old TABS NAVIGATION
pattern = re.compile(r'<!-- TM8 T00LS EXPANDABLE SECTION -->.*?</div>\s*<!-- TABS NAVIGATION -->.*?</div>', re.DOTALL)

new_tabs_nav = """<!-- TM8 T00LS EXPANDABLE SECTION -->
    <div style="width: 100%; max-width: 1000px; margin: 0 auto 32px auto; background: #000; border: 2px solid #00ffcc; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,255,204,0.15);">
        <details style="padding: 0;">
            <summary style="padding: 18px 24px; font-size: 1.3rem; font-weight: 900; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center; color: #fff; text-transform: uppercase; letter-spacing: 1px;">
                <span style="display: flex; align-items: center; gap: 10px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00ffcc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
                    TM8 T00LS
                </span>
                <span style="font-size: 0.8rem; background: #222; border: 1px solid #444; color: #fff; padding: 6px 12px; border-radius: 20px;">EXPAND MENU</span>
            </summary>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; padding: 20px; background: #111; border-top: 1px solid #333;">
                
                <button class="tm-btn tab-btn active" style="width: 100%; text-align: left; padding: 16px; background: #222; color: #fff; border: 1px solid #444; border-radius: 8px; font-size: 1rem; display: flex; justify-content: space-between; align-items: center; transition: all 0.2s ease;" onclick="switchTab('tab-stats')" onmouseover="this.style.borderColor='#fff'" onmouseout="this.style.borderColor='#444'">
                    <span>👤 Player Profile</span>
                    <span>→</span>
                </button>
                
                <button class="tm-btn tab-btn" style="width: 100%; text-align: left; padding: 16px; background: #222; color: #fff; border: 1px solid #444; border-radius: 8px; font-size: 1rem; display: flex; justify-content: space-between; align-items: center; transition: all 0.2s ease;" onclick="switchTab('tab-lessons')" onmouseover="this.style.borderColor='#fff'" onmouseout="this.style.borderColor='#444'">
                    <span>📓 Training Journal</span>
                    <span>→</span>
                </button>

                <button class="tm-btn tab-btn" style="width: 100%; text-align: left; padding: 16px; background: #000; color: #00ffcc; border: 1px solid #00ffcc; border-radius: 8px; font-size: 1rem; display: flex; justify-content: space-between; align-items: center; box-shadow: inset 0 0 10px rgba(0,255,204,0.1); transition: all 0.2s ease;" onclick="switchTab('tab-tools')" onmouseover="this.style.background='#00ffcc'; this.style.color='#000'" onmouseout="this.style.background='#000'; this.style.color='#00ffcc'">
                    <span style="font-weight: 900; letter-spacing: 1px;">⚡ RaQGeN PRO</span>
                    <span style="font-weight: 900;">→</span>
                </button>

            </div>
        </details>
    </div>"""

content = pattern.sub(new_tabs_nav, content, count=1)

# 2. Update the RaQGeN tab header to use an impressive SVG logo instead of simple text
raqgen_header_pattern = re.compile(r'<h3 style="color: #fff; margin: 0; display: flex; align-items: center; gap: 8px;">.*?</h3>', re.DOTALL)

new_raqgen_header = """<div style="display: flex; align-items: center; gap: 12px; margin: 0;">
                    <!-- Custom RaQGeN Logo SVG -->
                    <svg width="180" height="40" viewBox="0 0 200 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <!-- Geometric R -->
                        <path d="M10 5H30C38.2843 5 45 11.7157 45 20C45 23.4797 43.8166 26.6833 41.8028 29.2155L50 35H35L29 28H18V35H10V5ZM18 13V21H30C32.2091 21 34 19.2091 34 17C34 14.7909 32.2091 13 30 13H18Z" fill="#00ffcc"/>
                        <!-- Minimal a -->
                        <path d="M55 25C55 19.4772 59.4772 15 65 15H75V35H65C59.4772 35 55 30.5228 55 25ZM63 25C63 26.1046 63.8954 27 65 27H67V23H65C63.8954 23 63 23.8954 63 25Z" fill="#ffffff"/>
                        <!-- Crosshair Q -->
                        <path d="M85 20C85 11.7157 91.7157 5 100 5C108.284 5 115 11.7157 115 20C115 28.2843 108.284 35 100 35C91.7157 35 85 28.2843 85 20ZM93 20C93 23.866 96.134 27 100 27C103.866 27 107 23.866 107 20C107 16.134 103.866 13 100 13C96.134 13 93 16.134 93 20Z" fill="#00ffcc"/>
                        <path d="M100 13V5" stroke="#00ffcc" stroke-width="2"/>
                        <path d="M100 35V27" stroke="#00ffcc" stroke-width="2"/>
                        <path d="M85 20H93" stroke="#00ffcc" stroke-width="2"/>
                        <path d="M115 20H107" stroke="#00ffcc" stroke-width="2"/>
                        <path d="M109 29L120 40" stroke="#00ffcc" stroke-width="3" stroke-linecap="square"/>
                        <!-- Geometric G -->
                        <path d="M125 20C125 11.7157 131.716 5 140 5H150V13H140C136.134 13 133 16.134 133 20C133 23.866 136.134 27 140 27H142V20H150V35H140C131.716 35 125 28.2843 125 20Z" fill="#ffffff"/>
                        <!-- Minimal e -->
                        <path d="M155 25C155 19.4772 159.477 15 165 15H175V23H163C163 24.1046 163.895 25 165 25H175V35H165C159.477 35 155 30.5228 155 25Z" fill="#ffffff"/>
                        <!-- Sharp N -->
                        <path d="M180 35V5H188L195 20V5H200V35H192L185 20V35H180Z" fill="#00ffcc"/>
                    </svg>
                    <span style="font-size: 0.65rem; background: #00ffcc; color: #000; padding: 2px 8px; border-radius: 4px; font-weight: 900; letter-spacing: 1px; margin-top: 4px;">PRO</span>
                </div>"""

content = raqgen_header_pattern.sub(new_raqgen_header, content, count=1)

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Update complete")
