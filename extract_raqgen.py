import re

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'r', encoding='utf-8') as f:
    profile_content = f.read()

raqgen_div_pattern = re.compile(r'<div id="tab-tools" class="tab-content">(.*?)</div>\s*</div>\s*</div>', re.DOTALL)
match = raqgen_div_pattern.search(profile_content)
if match:
    with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/raqgen_tmp.html', 'w') as out:
        out.write(match.group(1))
    print("Extracted to raqgen_tmp.html")
