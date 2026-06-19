import glob
import re

new_sidebar = """<!-- Sidebar -->
                <aside class="sidebar">
                    
                    <!-- Lead Gen / Local Roster -->
                    <div class="sidebar-widget newsletter" style="background-color: var(--text); color: var(--bg);">
                        <h3 style="color: var(--bg);">Unlock the Journal</h3>
                        <p style="color: #ccc; margin-bottom: 1.5rem;">Join the local roster to get full access to all articles and priority booking for lessons in Hastings & Holdrege.</p>
                        <form class="newsletter-form">
                            <input type="email" placeholder="Email address" required style="border-color: var(--bg);">
                            <button type="submit" style="background: var(--bg); color: var(--text); border-color: var(--bg);">Get Access</button>
                        </form>
                    </div>

                    <!-- Coach's Bag -->
                    <div class="sidebar-widget gear-guide">
                        <h3>What's In My Bag</h3>
                        <ul class="gear-list">
                            <li style="padding-bottom: 1rem; border-bottom: 1px solid var(--border);">
                                <div class="gear-item">
                                    <strong>Head Gravity Tour 98</strong>
                                    <span>Current Racket</span>
                                </div>
                            </li>
                            <li style="padding-bottom: 1rem; border-bottom: 1px solid var(--border);">
                                <div class="gear-item">
                                    <strong>Confidential Mains / Mach 10 Crosses</strong>
                                    <span>String Setup (Solinco)</span>
                                </div>
                            </li>
                            <li style="padding-top: 0.5rem;">
                                <div class="gear-item">
                                    <strong>Solinco Overgrip</strong>
                                    <span>Grip</span>
                                </div>
                            </li>
                        </ul>
                    </div>

                </aside>"""

for filepath in glob.glob('/Users/adeningwerson/Desktop/Tennis-Landing-Page/blog/*.html'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # In case the inner pages use a different comment or just <aside class="sidebar">
    updated_content = re.sub(r'<aside class="sidebar">.*?</aside>', new_sidebar.replace("<!-- Sidebar -->\n                ", ""), content, flags=re.DOTALL)
    
    if updated_content != content:
        with open(filepath, 'w') as f:
            f.write(updated_content)
        print(f"Updated {filepath}")
