import re

files = [
    '/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html',
    '/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html'
]

old_text = "A.I. Personalized Racket Recommendation Engine. Powered by OSINT, TF-IDF Scraping, and the Mahalanobis Distance Equation."
new_text = "Personalized Racket Recommendation Engine. Powered by TennisMate's Equations, OSINT data, and the Mahalanobis Distance Model."

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
