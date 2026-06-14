import re

filepath = "/Users/adeningwerson/Desktop/Tennis-Landing-Page/blog/index.html"

with open(filepath, 'r') as f:
    content = f.read()

new_css = """
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap');
        
        :root { 
            --bg-primary: #0a0a0a; 
            --bg-secondary: #111111;
            --bg-tertiary: #1a1a1a;
            --text-primary: #ffffff; 
            --text-secondary: #a1a1aa; 
            --accent: #E1FF00; 
            --accent-hover: #cce600; 
            --border: #27272a; 
            --glow: rgba(225, 255, 0, 0.15);
        }
        
        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        body { 
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; 
            color: var(--text-primary); 
            background-color: var(--bg-primary); 
            line-height: 1.6; 
            -webkit-font-smoothing: antialiased;
            overflow-x: hidden;
            background-image: 
              radial-gradient(at 0% 0%, rgba(225, 255, 0, 0.03) 0px, transparent 50%),
              radial-gradient(at 100% 0%, rgba(26, 26, 26, 0.5) 0px, transparent 50%);
            background-attachment: fixed;
        }
        
        ::selection { background: var(--accent); color: #000; }
        a { color: inherit; text-decoration: none; }
        .container { width: 100%; max-width: 1100px; margin: 0 auto; padding: 0 24px; }
        
        /* Navigation (Glassmorphism) */
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
        
        nav { display: flex; justify-content: space-between; align-items: center; }
        
        .logo a { 
            font-weight: 900; 
            letter-spacing: -0.04em; 
            font-size: 1.3rem; 
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: 6px;
        }
        
        .logo span { color: var(--accent); }
        
        .nav-links { display: flex; gap: 24px; align-items: center; font-size: 0.95rem; font-weight: 500; }
        .nav-links a { color: var(--text-secondary); transition: color 0.2s; }
        .nav-links a:hover, .nav-links a.active { color: var(--text-primary); }
        
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
        .btn:hover { background: rgba(255,255,255,0.05); border-color: var(--text-primary); }
        
        main { padding: 140px 0 80px; }
        h1 { font-size: clamp(2.5rem, 5vw, 3.5rem); margin-bottom: 40px; letter-spacing: -0.04em; font-weight: 900; }

        /* New Layout Grid */
        .blog-layout { display: grid; grid-template-columns: 1fr 340px; gap: 48px; }
        @media (max-width: 900px) { .blog-layout { grid-template-columns: 1fr; } }
        
        /* Sponsor Ad Slot */
        .sponsor-banner { 
            background: rgba(26, 26, 26, 0.4); 
            backdrop-filter: blur(8px);
            border: 1px dashed rgba(255,255,255,0.15); 
            border-radius: 12px; 
            padding: 24px; 
            margin-bottom: 40px; 
            display: flex; 
            flex-direction: column; 
            gap: 8px; 
            transition: all 0.3s ease; 
        }
        .sponsor-banner:hover { border-color: var(--accent); transform: translateY(-2px); box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        .sponsor-label { font-size: 0.75rem; text-transform: uppercase; color: var(--text-secondary); letter-spacing: 0.1em; font-weight: 700; }
        .sponsor-content h3 { color: var(--text-primary); margin-bottom: 6px; font-size: 1.35rem; }
        .sponsor-content p { color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 12px; }
        
        .sponsor-link { 
            display: inline-block; 
            color: #000; 
            background: var(--accent); 
            padding: 10px 20px; 
            border-radius: 100px; 
            font-weight: 700; 
            font-size: 0.9rem; 
            align-self: flex-start;
            transition: all 0.2s ease;
            box-shadow: 0 0 15px var(--glow);
        }
        .sponsor-link:hover { background: var(--accent-hover); transform: translateY(-2px); box-shadow: 0 4px 20px rgba(225, 255, 0, 0.25); }

        .blog-grid { display: flex; flex-direction: column; gap: 32px; }
        
        .blog-card { 
            padding: 32px; 
            background: rgba(17, 17, 17, 0.6); 
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255,255,255,0.05); 
            border-radius: 12px; 
            transition: all 0.3s ease; 
            position: relative;
            overflow: hidden;
        }
        
        .blog-card:hover { 
            transform: translateY(-4px); 
            border-color: rgba(255,255,255,0.15); 
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }
        
        /* Subtle card glow on hover */
        .blog-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 1px;
            background: linear-gradient(90deg, transparent, var(--accent), transparent);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .blog-card:hover::before { opacity: 0.5; }
        
        .blog-card .category { color: var(--accent); font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 12px; display: inline-block; background: rgba(225,255,0,0.1); padding: 4px 12px; border-radius: 100px; }
        .blog-card h2 { font-size: 1.6rem; margin-bottom: 12px; letter-spacing: -0.02em; font-weight: 700; }
        .blog-card p { color: var(--text-secondary); font-size: 1.05rem; margin-bottom: 24px; line-height: 1.7; }
        .read-more { color: var(--text-primary); font-weight: 600; font-size: 0.95rem; display: inline-flex; align-items: center; gap: 8px; border-bottom: 1px solid var(--accent); padding-bottom: 2px; transition: all 0.2s; }
        .read-more:hover { color: var(--accent); border-bottom-color: transparent; }

        /* Sidebar Monetization */
        .sidebar { display: flex; flex-direction: column; gap: 24px; position: sticky; top: 100px; align-self: start; }
        
        .sidebar-widget { 
            background: rgba(17, 17, 17, 0.6); 
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255,255,255,0.05); 
            border-radius: 12px; 
            padding: 32px; 
        }
        .sidebar-widget h3 { font-size: 1.3rem; margin-bottom: 12px; letter-spacing: -0.02em; color: var(--text-primary); }
        .sidebar-widget h3 span { color: var(--accent); }
        .sidebar-widget p { color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 24px; line-height: 1.6; }
        
        .btn-primary { 
            background: var(--accent); 
            color: #000; 
            display: block; 
            text-align: center; 
            width: 100%; 
            font-weight: 700; 
            padding: 14px 24px; 
            border-radius: 100px; 
            border: none; 
            cursor: pointer; 
            text-decoration: none; 
            transition: all 0.2s ease;
            box-shadow: 0 0 20px var(--glow);
        }
        .btn-primary:hover { background: var(--accent-hover); transform: translateY(-2px); box-shadow: 0 4px 25px rgba(225, 255, 0, 0.25); }

        /* Gear List Affiliate Block */
        .gear-list { list-style: none; margin-bottom: 20px; display: flex; flex-direction: column; gap: 12px; }
        .gear-list a { 
            display: block; 
            padding: 16px; 
            background: rgba(10, 10, 10, 0.8); 
            border: 1px solid rgba(255,255,255,0.05); 
            border-radius: 8px; 
            transition: all 0.2s ease; 
        }
        .gear-list a:hover { border-color: rgba(255,255,255,0.2); background: rgba(26,26,26,0.8); transform: translateX(4px); }
        .gear-item { display: flex; flex-direction: column; gap: 4px; }
        .gear-item strong { font-size: 0.95rem; color: var(--text-primary); }
        .gear-item span { font-size: 0.85rem; color: var(--text-secondary); }
        .view-all { color: var(--text-primary); font-size: 0.9rem; font-weight: 600; border-bottom: 1px solid var(--border); padding-bottom: 2px; transition: all 0.2s; }
        .view-all:hover { color: var(--accent); border-bottom-color: var(--accent); }

        /* Lead Gen / Newsletter */
        .newsletter-form { display: flex; flex-direction: column; gap: 12px; }
        .newsletter-form input { 
            padding: 14px 16px; 
            border: 1px solid rgba(255,255,255,0.1); 
            border-radius: 8px; 
            background: rgba(10, 10, 10, 0.8); 
            color: var(--text-primary); 
            font-family: inherit; 
            font-size: 0.95rem; 
            transition: all 0.2s ease;
        }
        .newsletter-form input:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 1px var(--accent); }
        .newsletter-form button { 
            padding: 14px; 
            border-radius: 100px; 
            font-weight: 700; 
            background: var(--text-primary); 
            color: #000; 
            border: none; 
            cursor: pointer; 
            font-family: inherit; 
            font-size: 0.95rem; 
            transition: all 0.2s; 
        }
        .newsletter-form button:hover { background: #e4e4e7; transform: translateY(-2px); }
"""

content = re.sub(r'<style>.*?</style>', f'<style>\n{new_css}\n    </style>', content, flags=re.DOTALL)

with open(filepath, 'w') as f:
    f.write(content)

print("Updated blog/index.html")
