import os
import glob
import re

blog_css = """
    /* ===== Elite Blog Styling (Tennis T-Mate) ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap');
    
    :root {
      --bg-primary: #0a0a0a;
      --bg-secondary: #111111;
      --bg-tertiary: #1a1a1a;
      --text-primary: #ffffff;
      --text-secondary: #a1a1aa;
      --accent: #E1FF00; /* Optic Yellow */
      --accent-hover: #cce600;
      --border: #27272a;
      --glow: rgba(225, 255, 0, 0.15);
    }
    
    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      color: var(--text-primary);
      background-color: var(--bg-primary);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      /* Subtle mesh gradient background */
      background-image: 
        radial-gradient(at 0% 0%, rgba(225, 255, 0, 0.03) 0px, transparent 50%),
        radial-gradient(at 100% 0%, rgba(26, 26, 26, 0.5) 0px, transparent 50%);
      background-attachment: fixed;
    }
    
    ::selection {
      background: var(--accent);
      color: #000;
    }
    
    /* ===== Navigation (Glassmorphism) ===== */
    header {
      position: fixed;
      top: 0;
      width: 100%;
      z-index: 100;
      background: rgba(10, 10, 10, 0.7);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      padding: 16px 0;
      transition: all 0.3s ease;
    }
    
    nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    
    .logo a {
      font-weight: 900;
      letter-spacing: -0.04em;
      font-size: 1.3rem;
      color: var(--text-primary);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    
    .logo span { color: var(--accent); }
    
    .nav-links {
      display: flex;
      gap: 24px;
      align-items: center;
      font-size: 0.95rem;
      font-weight: 500;
    }
    
    .nav-links a {
      color: var(--text-secondary);
      text-decoration: none;
      transition: color 0.2s;
    }
    
    .nav-links a:hover { color: var(--text-primary); }
    
    /* Buttons */
    .btn {
      padding: 10px 24px;
      border-radius: 100px;
      font-weight: 600;
      border: 1px solid rgba(255,255,255,0.2);
      color: var(--text-primary);
      background: transparent;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    
    .btn:hover {
      background: rgba(255,255,255,0.05);
      border-color: var(--text-primary);
    }
    
    .btn-primary {
      background: var(--accent);
      color: #000;
      border: none;
      padding: 14px 32px;
      font-weight: 700;
      border-radius: 100px;
      text-decoration: none;
      display: inline-block;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      box-shadow: 0 0 20px var(--glow);
    }
    
    .btn-primary:hover {
      background: var(--accent-hover);
      transform: translateY(-2px);
      box-shadow: 0 4px 25px rgba(225, 255, 0, 0.25);
    }
    
    /* ===== Reading Progress Bar ===== */
    .progress-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: transparent;
      z-index: 101;
    }
    
    .progress-bar {
      height: 3px;
      background: var(--accent);
      width: 0%;
      box-shadow: 0 0 10px var(--accent);
    }
    
    /* ===== Main Content Area ===== */
    .container {
      width: 100%;
      max-width: 720px;
      margin: 0 auto;
      padding: 0 24px;
    }
    
    main {
      padding: 140px 0 80px; /* Offset for fixed header */
    }
    
    /* Typography */
    .eyebrow {
      color: var(--accent);
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.15em;
      margin-bottom: 20px;
      display: inline-block;
      background: rgba(225, 255, 0, 0.1);
      padding: 4px 12px;
      border-radius: 100px;
      border: 1px solid rgba(225, 255, 0, 0.2);
    }
    
    h1 {
      font-size: clamp(2.5rem, 5vw, 4rem);
      line-height: 1.1;
      margin-bottom: 24px;
      letter-spacing: -0.04em;
      font-weight: 900;
      text-wrap: balance;
    }
    
    .meta {
      color: var(--text-secondary);
      font-size: 1rem;
      margin-bottom: 56px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 32px;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    
    /* Author avatar placeholder */
    .meta::before {
      content: '';
      display: block;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--bg-tertiary), var(--border));
      border: 1px solid rgba(255,255,255,0.1);
    }
    
    /* Article Body Formatting */
    article {
      font-size: 1.15rem;
      color: #d4d4d8; /* Slightly brighter than text-secondary for readability */
    }
    
    /* Drop Cap for first paragraph */
    article > p:first-of-type::first-letter {
      float: left;
      font-size: 4.5rem;
      line-height: 0.8;
      padding-right: 12px;
      padding-top: 4px;
      font-weight: 900;
      color: var(--text-primary);
    }
    
    article p { margin-bottom: 28px; }
    
    article a {
      color: var(--text-primary);
      text-decoration: underline;
      text-decoration-color: var(--accent);
      text-decoration-thickness: 2px;
      text-underline-offset: 4px;
      transition: color 0.2s, text-decoration-color 0.2s;
    }
    
    article a:hover {
      color: var(--accent);
    }
    
    article h2 {
      font-size: 2rem;
      margin: 56px 0 24px;
      color: var(--text-primary);
      letter-spacing: -0.02em;
    }
    
    article h3 {
      font-size: 1.4rem;
      margin: 40px 0 16px;
      color: var(--text-primary);
    }
    
    article strong { color: var(--text-primary); }
    
    /* Glassmorphism Affiliate/Callout Box */
    .affiliate-box {
      background: rgba(26, 26, 26, 0.4);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-left: 4px solid var(--accent);
      padding: 32px;
      margin: 48px 0;
      border-radius: 0 12px 12px 0;
      position: relative;
      overflow: hidden;
    }
    
    /* Subtle glow inside the box */
    .affiliate-box::after {
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: radial-gradient(circle, rgba(225, 255, 0, 0.05) 0%, transparent 70%);
      pointer-events: none;
    }
    
    .affiliate-box h4 {
      font-size: 1.2rem;
      margin-bottom: 12px;
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    
    .affiliate-box p {
      margin-bottom: 0;
      font-size: 1.05rem;
    }
    
    /* Email Capture CTA Box */
    .cta-box {
      background: radial-gradient(120% 100% at 50% 0%, var(--bg-tertiary) 0%, var(--bg-secondary) 100%);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 48px;
      border-radius: 16px;
      margin-top: 80px;
      text-align: center;
      position: relative;
      box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
    
    .cta-box h3 {
      font-size: 1.75rem;
      margin-bottom: 16px;
      color: var(--text-primary);
    }
    
    .cta-box p {
      margin-bottom: 32px;
      color: var(--text-secondary);
    }
    
    /* Lists */
    article ul, article ol {
      margin-bottom: 28px;
      padding-left: 24px;
    }
    
    article li {
      margin-bottom: 12px;
      padding-left: 8px;
    }
    
    article li::marker {
      color: var(--accent);
    }
"""

js_injection = """
  <!-- Scroll Progress Script -->
  <script>
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      const bar = document.getElementById('reading-progress');
      if(bar) bar.style.width = scrolled + '%';
    });
  </script>
"""

progress_html = """
  <div class="progress-container">
    <div class="progress-bar" id="reading-progress"></div>
  </div>
"""

blog_dir = "/Users/adeningwerson/Desktop/Tennis-Landing-Page/blog"

for filename in os.listdir(blog_dir):
    if filename.endswith(".html") and filename != "index.html":
        filepath = os.path.join(blog_dir, filename)
        with open(filepath, 'r') as f:
            content = f.read()
            
        # Replace styles
        content = re.sub(r'<style>.*?</style>', f'<style>{blog_css}</style>', content, flags=re.DOTALL)
        
        # Inject progress bar if not exists
        if 'class="progress-container"' not in content:
            content = content.replace('<body>', f'<body>\n{progress_html}')
            
        # Inject JS if not exists
        if 'id="reading-progress"' not in content and 'Scroll Progress Script' not in content:
            content = content.replace('</body>', f'{js_injection}\n</body>')
            
        # Update nav to match new structure
        nav_pattern = r'<div class="logo"><a href="/"[^>]*>TENNIS <span>T-MATE</span></a></div>'
        new_nav = '<div class="logo"><a href="/">TENNIS <span>T-MATE</span></a></div>'
        content = re.sub(nav_pattern, new_nav, content)
        
        with open(filepath, 'w') as f:
            f.write(content)
            
print("Successfully upgraded individual blog pages.")
