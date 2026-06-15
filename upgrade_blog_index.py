import re

filepath = "/Users/adeningwerson/Desktop/Tennis-Landing-Page/blog/index.html"

with open(filepath, 'r') as f:
    content = f.read()

new_css = """
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
        text-transform: uppercase;
    }
    
    h1 { font-size: clamp(3rem, 8vw, 6rem); margin-bottom: 2rem; word-wrap: break-word; }

    a { color: var(--text); text-decoration: none; }
    
    .container {
        width: 100%;
        max-width: 1200px;
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
    }

    .logo { font-size: 1.5rem; font-weight: 900; letter-spacing: -0.04em; }

    .nav-links { display: flex; gap: 2rem; align-items: center; font-size: 0.9rem; font-weight: 700; }
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
    }
    .btn:hover { background-color: var(--bg); color: var(--text); }

    .btn-primary {
        background: var(--text);
        color: var(--bg);
        display: block;
        text-align: center;
        width: 100%;
        padding: 14px 24px;
        font-weight: 700;
        text-transform: uppercase;
        border: 1px solid var(--text);
        transition: all 0.2s;
    }
    .btn-primary:hover { background: var(--bg); color: var(--text); }

    /* New Layout Grid */
    .blog-layout { display: grid; grid-template-columns: 1fr 340px; gap: 48px; border-top: 1px solid var(--border-dark); padding-top: 4rem; }
    @media (max-width: 900px) { .blog-layout { grid-template-columns: 1fr; } }
    
    .blog-grid { display: flex; flex-direction: column; }
    
    .blog-card { 
        padding: 2rem 0; 
        border-bottom: 1px solid var(--border);
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    
    .blog-card:last-child { border-bottom: none; }
    
    .blog-card .category { 
        font-size: 0.75rem; 
        font-weight: 700; 
        text-transform: uppercase; 
        letter-spacing: 0.05em; 
        margin-bottom: 1rem; 
        color: var(--text-muted);
    }
    .blog-card h2 { font-size: 2rem; margin-bottom: 1rem; }
    .blog-card p { color: var(--text-muted); font-size: 1.1rem; margin-bottom: 1.5rem; }
    .read-more { font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border-bottom: 1px solid var(--text); padding-bottom: 2px; }

    /* Sidebar Monetization */
    .sidebar { display: flex; flex-direction: column; gap: 48px; position: sticky; top: 40px; align-self: start; }
    
    .sidebar-widget { 
        border: 1px solid var(--border-dark);
        padding: 2rem;
    }
    .sidebar-widget h3 { font-size: 1.5rem; margin-bottom: 1rem; }
    .sidebar-widget p { color: var(--text-muted); font-size: 1rem; margin-bottom: 1.5rem; }
    
    /* Gear List Affiliate Block */
    .gear-list { list-style: none; display: flex; flex-direction: column; gap: 1rem; margin-bottom: 1.5rem; }
    .gear-list a { 
        display: block; 
        padding-bottom: 1rem;
        border-bottom: 1px solid var(--border);
    }
    .gear-list a:hover strong { text-decoration: underline; }
    .gear-item { display: flex; flex-direction: column; }
    .gear-item strong { font-size: 1rem; text-transform: uppercase; margin-bottom: 0.25rem; }
    .gear-item span { font-size: 0.85rem; color: var(--text-muted); }
    .view-all { font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border-bottom: 1px solid var(--text); padding-bottom: 2px; }

    /* Lead Gen / Newsletter */
    .newsletter-form { display: flex; flex-direction: column; gap: 1rem; }
    .newsletter-form input { 
        padding: 12px 16px; 
        border: 1px solid var(--border-dark);
        background: var(--bg);
        color: var(--text);
        font-family: inherit; 
        font-size: 1rem; 
    }
    .newsletter-form input:focus { outline: none; border-width: 2px; }
    .newsletter-form button { 
        padding: 12px; 
        font-weight: 700; 
        text-transform: uppercase;
        background: var(--text); 
        color: var(--bg); 
        border: 1px solid var(--text);
        cursor: pointer; 
        font-family: inherit; 
    }
"""

content = re.sub(r'<style>.*?</style>', f'<style>\\n{new_css}\\n    </style>', content, flags=re.DOTALL)

# Replace the header to be consistent
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
content = re.sub(r'<header>.*?</header>', nav_replacement, content, flags=re.DOTALL)

with open(filepath, 'w') as f:
    f.write(content)

print("Updated blog/index.html to brutalist CSS")
