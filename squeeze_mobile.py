import re

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Compress mobile hero-desc margin
content = content.replace(
    '.hero-desc { grid-column: 1 / -1; margin-bottom: 2rem; }',
    '.hero-desc { grid-column: 1 / -1; margin-bottom: 1rem; }'
)

# 2. Compress mobile stats-marquee margins
content = content.replace(
    '.stats-marquee { display: flex; gap: 2rem; margin-top: 1.5rem; }',
    '.stats-marquee { display: flex; gap: 1rem; margin-top: 1rem; flex-wrap: wrap; }'
)

# 3. Compress the top margin of the TM8 T00LS container
content = content.replace(
    '<div class="container" style="position: relative; z-index: 10; margin-top: 20px; margin-bottom: 40px; max-width: 1000px;">',
    '<div class="container" style="position: relative; z-index: 10; margin-top: 0px; margin-bottom: 40px; max-width: 1000px;">'
)

# 4. Shrink the H1 bottom margin generally to save a bit more
content = re.sub(
    r'\.hero h1 \{\n\s*grid-column: 1 / -1;\n\s*font-size: clamp\(3rem, 9vw, 8rem\);\n\s*margin-bottom: 1rem;\n\s*word-wrap: break-word;\n\s*line-height: 1;\n\s*\}',
    r'.hero h1 {\n            grid-column: 1 / -1;\n            font-size: clamp(2.8rem, 9vw, 8rem);\n            margin-bottom: 0.5rem;\n            word-wrap: break-word;\n            line-height: 1;\n        }',
    content
)

# 5. Shrink nav padding even more
content = re.sub(
    r'nav \{\n\s*padding: 16px 0;\n\s*border-bottom: 1px solid var\(--border-dark\);\n\s*\}',
    r'nav {\n            padding: 12px 0;\n            border-bottom: 1px solid var(--border-dark);\n        }',
    content
)

# 6. Shrink hero top padding
content = re.sub(
    r'\.hero \{\n\s*padding: 40px 0 20px 0;',
    r'.hero {\n            padding: 20px 0 10px 0;',
    content
)


with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile CSS squeezed.")
