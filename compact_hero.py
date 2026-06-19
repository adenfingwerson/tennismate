import re

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Nav Padding
content = re.sub(
    r'nav {\s*padding: 24px 0;\s*border-bottom: 1px solid var\(--border-dark\);\s*}',
    r'nav {\n            padding: 16px 0;\n            border-bottom: 1px solid var(--border-dark);\n        }',
    content,
    flags=re.DOTALL
)

# 2. Hero Padding and Min-Height
content = re.sub(
    r'\.hero \{\s*padding: 120px 0;\s*min-height: 70vh;\s*display: flex;\s*align-items: center;\s*border-bottom: 1px solid var\(--border-dark\);\s*\}',
    r'.hero {\n            padding: 40px 0 20px 0;\n            min-height: auto;\n            display: flex;\n            align-items: center;\n            border-bottom: none;\n        }',
    content,
    flags=re.DOTALL
)

# 3. Hero H1 Margin and Line Height
content = re.sub(
    r'\.hero h1 \{\s*grid-column: 1 / -1;\s*font-size: clamp\(4rem, 11vw, 10rem\);\s*margin-bottom: 2rem;\s*word-wrap: break-word;\s*\}',
    r'.hero h1 {\n            grid-column: 1 / -1;\n            font-size: clamp(3rem, 9vw, 8rem);\n            margin-bottom: 1rem;\n            word-wrap: break-word;\n            line-height: 1;\n        }',
    content,
    flags=re.DOTALL
)

# 4. Stats Marquee CSS
content = re.sub(
    r'\.stats-marquee \{\s*grid-column: 1 / -1;\s*margin-top: 6rem;\s*display: flex;\s*gap: 4rem;\s*border-top: 1px solid var\(--border-dark\);\s*padding-top: 1\.5rem;\s*\}',
    r'.stats-marquee {\n            grid-column: 1 / -1;\n            margin-top: 2rem;\n            margin-bottom: 0rem;\n            display: flex;\n            flex-wrap: wrap;\n            gap: 3rem;\n            border-top: 1px solid var(--border-dark);\n            padding-top: 1rem;\n        }',
    content,
    flags=re.DOTALL
)

# 5. Mobile Stats Marquee visibility
content = re.sub(
    r'\.stats-marquee \{ display: none; \}',
    r'.stats-marquee { display: flex; gap: 2rem; margin-top: 1.5rem; }',
    content
)

# 6. TM8 T00LS Container margin
content = re.sub(
    r'<div class="container" style="position: relative; z-index: 10; margin-top: -30px; margin-bottom: 60px; max-width: 1000px;">',
    r'<div class="container" style="position: relative; z-index: 10; margin-top: 20px; margin-bottom: 40px; max-width: 1000px;">',
    content
)

# Also let's adjust hero-cta margin to save space
content = re.sub(
    r'\.hero-cta \{\s*grid-column: 8 / -1;\s*display: flex;\s*flex-direction: column;\s*align-items: flex-start;\s*gap: 1rem;\s*\}',
    r'.hero-cta {\n            grid-column: 8 / -1;\n            display: flex;\n            flex-direction: column;\n            align-items: flex-start;\n            gap: 0.5rem;\n        }',
    content,
    flags=re.DOTALL
)

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied compact hero styles.")
