import glob
import re

# Remove from individual blog posts
for filepath in glob.glob('/Users/adeningwerson/Desktop/Tennis-Landing-Page/blog/*.html'):
    if 'index.html' in filepath:
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Remove the whole Join the Local Roster section and the script
    content = re.sub(r'<div style="background-color: var\(--text\); color: var\(--bg\); padding: 32px;">.*?</div>\s*<div style="padding: 32px;', r'<div style="padding: 32px;', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*document\.getElementById\(\'subscribe-form\'\).*?</script>', '', content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Removed form from {filepath}")

# Remove from blog index
with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/blog/index.html', 'r') as f:
    content = f.read()

# Remove the newsletter sidebar widget
content = re.sub(r'<!-- Lead Gen / Local Roster -->\s*<div class="sidebar-widget newsletter".*?</div>', '', content, flags=re.DOTALL)

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/blog/index.html', 'w') as f:
    f.write(content)
print("Removed form from blog index")
