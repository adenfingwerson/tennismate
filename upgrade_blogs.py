import os
import glob
import re

blog_css = """
    /* ===== Minimalist Editorial / Brutalist Architecture ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap');

    :root {
        --bg: #ffffff;
        --text: #000000;
        --text-muted: #666666;
        --border: #e5e5e5;
        --border-dark: #000000;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
        font-family: 'Inter', -apple-system, sans-serif;
        color: var(--text);
        background-color: var(--bg);
        line-height: 1.6;
        -webkit-font-smoothing: antialiased;
    }

    h1, h2, h3, h4 {
        font-weight: 900;
        letter-spacing: -0.04em;
        line-height: 1.05;
        color: var(--text);
    }
    
    h1 { font-size: clamp(3rem, 8vw, 5rem); text-transform: uppercase; word-wrap: break-word; }
    h2 { font-size: 2rem; margin: 4rem 0 1.5rem; text-transform: uppercase; }
    h3 { font-size: 1.5rem; margin: 2rem 0 1rem; }

    a { color: var(--text); text-decoration: underline; }
    
    .container {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
        padding: 0 24px;
    }

    /* ===== Navigation ===== */
    nav {
        padding: 24px 0;
        border-bottom: 1px solid var(--border-dark);
        margin-bottom: 80px;
    }

    nav .container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
    }

    .logo { font-size: 1.5rem; font-weight: 900; letter-spacing: -0.04em; text-transform: uppercase; text-decoration: none; }
    .logo a { text-decoration: none; }

    .nav-links { display: flex; gap: 2rem; align-items: center; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; }
    .nav-links a { text-decoration: none; }
    .nav-links a:hover { text-decoration: underline; }

    .btn {
        display: inline-block;
        background-color: var(--text);
        color: var(--bg);
        padding: 12px 24px;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        border: 1px solid var(--text);
        cursor: pointer;
        transition: all 0.2s;
        text-decoration: none;
    }
    .btn:hover { background-color: var(--bg); color: var(--text); }

    /* ===== Typography Helpers ===== */
    .kicker, .eyebrow {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 1.5rem;
        display: block;
        color: var(--text-muted);
    }

    /* ===== Article Structure ===== */
    .meta {
        font-size: 0.9rem;
        color: var(--text-muted);
        border-bottom: 1px solid var(--border-dark);
        padding-bottom: 2rem;
        margin-bottom: 4rem;
        font-weight: 500;
        text-transform: uppercase;
    }

    article { font-size: 1.2rem; color: var(--text); }
    
    article p { margin-bottom: 2rem; }
    
    /* Drop Cap */
    article > p:first-of-type::first-letter {
        float: left;
        font-size: 5rem;
        line-height: 0.8;
        padding-right: 12px;
        padding-top: 8px;
        font-weight: 900;
        color: var(--text);
    }

    /* ===== Affiliate / Callout Boxes ===== */
    .affiliate-box, .cta-box {
        border: 1px solid var(--border-dark);
        padding: 2rem;
        margin: 4rem 0;
        background: var(--bg);
    }

    .affiliate-box h4, .cta-box h3 {
        font-size: 1.25rem;
        margin-bottom: 1rem;
        text-transform: uppercase;
    }

    .affiliate-box p, .cta-box p {
        font-size: 1rem;
        margin-bottom: 1.5rem;
        color: var(--text-muted);
    }

    /* Lists */
    ul, ol { margin-bottom: 2rem; padding-left: 1.5rem; }
    li { margin-bottom: 0.5rem; }
    
    footer { border-top: 1px solid var(--border-dark); padding: 4rem 0; margin-top: 8rem; }
"""

blog_dir = "/Users/adeningwerson/Desktop/Tennis-Landing-Page/blog"

for filename in os.listdir(blog_dir):
    if filename.endswith(".html") and filename != "index.html":
        filepath = os.path.join(blog_dir, filename)
        with open(filepath, 'r') as f:
            content = f.read()
            
        # Replace styles entirely
        content = re.sub(r'<style>.*?</style>', f'<style>{blog_css}</style>', content, flags=re.DOTALL)
        
        # Remove old elements
        content = re.sub(r'<div class="progress-container">.*?</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- Scroll Progress Script -->.*?</script>', '', content, flags=re.DOTALL)
        
        # Rewrite the nav structure for brutalism
        nav_replacement = '''
    <nav>
        <div class="container">
            <div class="logo"><a href="/">Tennis T-Mate</a></div>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/blog/">Journal</a>
                <a href="https://cal.com/tennis-t-mate-hcmfls" class="btn">Book</a>
            </div>
        </div>
    </nav>
'''
        # We need to replace the old <header> block entirely
        content = re.sub(r'<header>.*?</header>', nav_replacement, content, flags=re.DOTALL)
        
        # Ensure main has standard padding
        content = re.sub(r'<main>.*?</main>', lambda m: m.group(0).replace('padding: 140px 0 80px;', 'padding: 40px 0;'), content, flags=re.DOTALL)

        with open(filepath, 'w') as f:
            f.write(content)
            
print("Upgraded individual blog pages to Brutalism.")
