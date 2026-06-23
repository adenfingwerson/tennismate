import os
import glob

def fix_fonts(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Increase small font sizes
    content = content.replace("font-size: 0.75rem", "font-size: 0.95rem")
    content = content.replace("font-size: 0.85rem", "font-size: 1rem")
    content = content.replace("font-size: 0.9rem", "font-size: 1rem")
    content = content.replace("font-size: 0.8em", "font-size: 0.9em")

    with open(filepath, 'w') as f:
        f.write(content)

for f in glob.glob("/Users/adeningwerson/Desktop/Tennis-Landing-Page/*.html"):
    fix_fonts(f)

print("Applied font size fixes.")
