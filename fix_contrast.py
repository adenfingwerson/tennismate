import os
import glob

def fix_html_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # If it has the old root, let's fix it (or we can just replace specific strings)
    old_root_1 = """        :root {
            --bg: #F40C3F;
            --bg-card: #F40C3F;
            --text: #160000;
            --text-muted: rgba(22, 0, 0, 0.6);
            --border: #160000;
            --border-dark: #160000;
            --accent: #160000;
            --accent-hover: #000000;
            --radius-pill: 0px;
            --radius-card: 0px;
            --shadow-soft: none;
        }"""
    
    new_root = """        :root {
            --bg: #FAFAFA;
            --bg-card: #FFFFFF;
            --text: #111827;
            --text-muted: #4B5563;
            --border: #E5E7EB;
            --border-dark: #111827;
            --accent: #F40C3F;
            --accent-hover: #D90A36;
            --radius-pill: 0px;
            --radius-card: 0px;
            --shadow-soft: none;
        }"""
        
    old_root_2 = """        :root {
            --bg: #F40C3F;
            --bg-card: #F40C3F;
            --text: #160000;
            --text-muted: rgba(22, 0, 0, 0.6);
            --border: #160000;
            --border-dark: #160000;
            --accent: #160000;
            --accent-hover: #000000;"""
            
    # Remove noise opacity
    content = content.replace("opacity: 0.4;", "opacity: 0.03;")
    content = content.replace("opacity: 0.5;", "opacity: 0.03;")
    content = content.replace("font-weight: 900;", "font-weight: 800;")
    
    # Try replacing root specifically
    if old_root_1 in content:
        content = content.replace(old_root_1, new_root)
    elif old_root_2 in content:
        # manual replace
        content = content.replace("--bg: #F40C3F;", "--bg: #FAFAFA;")
        content = content.replace("--bg-card: #F40C3F;", "--bg-card: #FFFFFF;")
        content = content.replace("--text: #160000;", "--text: #111827;")
        content = content.replace("--text-muted: rgba(22, 0, 0, 0.6);", "--text-muted: #4B5563;")
        content = content.replace("--border: #160000;", "--border: #E5E7EB;")
        content = content.replace("--border-dark: #160000;", "--border-dark: #111827;")
        content = content.replace("--accent: #160000;", "--accent: #F40C3F;")
        content = content.replace("--accent-hover: #000000;", "--accent-hover: #D90A36;")

    # Fix body font size
    content = content.replace("line-height: 1.5;", "line-height: 1.6;\n            font-size: 1.125rem;")

    with open(filepath, 'w') as f:
        f.write(content)
        
html_files = glob.glob("/Users/adeningwerson/Desktop/Tennis-Landing-Page/*.html")
for f in html_files:
    fix_html_file(f)

print("Applied contrast and readability fixes.")
