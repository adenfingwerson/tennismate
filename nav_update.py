import re

nav_dropdown_html_index = """<div class="nav-links" style="position: relative; display: flex; align-items: center; gap: 1rem;">
                <a href="/admin.html" id="admin-link" style="display: none; color: #000; border: 2px solid #000; padding: 6px 12px; background: #ccff00; text-decoration: none; font-weight: 900; text-transform: uppercase;">Admin</a>
                
                <details class="nav-dropdown" style="position: relative;">
                    <style>
                        .nav-dropdown summary::-webkit-details-marker { display: none; }
                        .nav-dropdown[open] summary { transform: translate(-2px, -2px); box-shadow: 6px 6px 0px var(--border-dark); }
                        .tm8-nav-item {
                            padding: 16px 20px; border-bottom: 2px solid var(--border-dark); text-decoration: none; color: var(--text); font-weight: 900; text-transform: uppercase; font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center; background: #fff; transition: background 0.15s ease;
                        }
                        .tm8-nav-item:hover { background: #f4f4f4; }
                        .tm8-nav-item.accent { background: linear-gradient(135deg, #ccff00 0%, #aadd00 100%); border-bottom: none; }
                        .tm8-nav-item.accent:hover { background: linear-gradient(135deg, #d4ff33 0%, #b8e600 100%); }
                    </style>
                    <summary style="list-style: none; cursor: pointer; display: flex; align-items: center; gap: 8px; font-weight: 900; text-transform: uppercase; border: 3px solid var(--border-dark); padding: 10px 20px; background: #fff; box-shadow: 4px 4px 0px var(--border-dark); transition: transform 0.1s, box-shadow 0.1s; font-size: 0.9rem;" onmouseover="this.style.transform='translate(-2px, -2px)'; this.style.boxShadow='6px 6px 0px var(--border-dark)';" onmouseout="if(!this.parentElement.open){this.style.transform='translate(0, 0)'; this.style.boxShadow='4px 4px 0px var(--border-dark)';}">
                        <span class="pulse-dot" style="width: 10px; height: 10px;"></span>
                        TM8 T00LS <span style="font-size: 0.7rem; margin-left: 4px;">▼</span>
                    </summary>
                    <div style="position: absolute; top: calc(100% + 14px); right: 0; background: #fff; border: 4px solid var(--border-dark); box-shadow: 8px 8px 0px var(--border-dark); width: 280px; display: flex; flex-direction: column; z-index: 1000;">
                        <a href="/profile.html?tab=stats" class="tm8-nav-item">
                            <span>Player Profile</span><span>→</span>
                        </a>
                        <a href="/profile.html?tab=lessons" class="tm8-nav-item">
                            <span>Coaching Notes</span><span>→</span>
                        </a>
                        <a href="/blog/" class="tm8-nav-item">
                            <span>The Journal</span><span>→</span>
                        </a>
                        <a href="/index.html#raqgen" class="tm8-nav-item" onclick="document.querySelector('.raqgen-section').scrollIntoView({behavior: 'smooth'}); return false;">
                            <span>RaQGeN Engine</span><span>→</span>
                        </a>
                        <a href="#" onclick="openModal(event)" class="tm8-nav-item accent">
                            <span>Book a Lesson</span><span>→</span>
                        </a>
                    </div>
                </details>
            </div>"""

nav_dropdown_html_profile = nav_dropdown_html_index.replace(
    '<a href="#" onclick="openModal(event)" class="tm8-nav-item accent">',
    '<a href="https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01" class="tm8-nav-item accent">'
).replace(
    'onclick="document.querySelector(\'.raqgen-section\').scrollIntoView({behavior: \'smooth\'}); return false;"',
    '' # Remove smooth scroll logic on profile since it redirects
)

def replace_nav(filepath, new_nav):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to match <div class="nav-links">...</div>
    pattern = re.compile(r'<div class="nav-links">.*?</div>', re.DOTALL)
    content = pattern.sub(new_nav, content, count=1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated nav in {filepath}")

replace_nav('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', nav_dropdown_html_index)
replace_nav('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', nav_dropdown_html_profile)
