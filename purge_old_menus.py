import re

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the massive master accordion from index.html body
content = re.sub(r'<!-- TM8 T00LS EXPANDABLE SECTION -->.*?</details>\s*</div>\s*</div>', '', content, flags=re.DOTALL)

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', 'w', encoding='utf-8') as f:
    f.write(content)


with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'r', encoding='utf-8') as f:
    p_content = f.read()

# Clean up profile.html (ensure bottom menu is gone, we already replaced the top one in previous steps but let's double check there isn't a lingering one)
p_content = re.sub(r'<!-- BOTTOM TM8 T00LS EXPANDABLE SECTION -->.*?</details>\s*</div>', '', p_content, flags=re.DOTALL)

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'w', encoding='utf-8') as f:
    f.write(p_content)

print("Old menus purged.")
