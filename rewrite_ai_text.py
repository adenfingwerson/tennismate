files = [
    '/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html',
    '/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html'
]

old_text = "TennisMate's Equations"
new_text = "TennisT-Mate's Equations"

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Text not found in {filepath}")
