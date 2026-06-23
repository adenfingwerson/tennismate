import re

files = ['/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', '/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html']

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # ensure tw_ratings is calculated
    if "let tw_ratings = calcTWMetrics" not in content:
        content = content.replace("let safe_score = Math.max(0, Math.min(100, 100 - (safety_cost * 2.5)));", "let safe_score = Math.max(0, Math.min(100, 100 - (safety_cost * 2.5)));\\n        let tw_ratings = calcTWMetrics(r, ideal_SW);")
        
    # fix literal newlines if they still exist somehow
    content = content.replace("\\n        let tw_ratings", "\n        let tw_ratings")
    content = content.replace("\\n            tw_ratings", "\n            tw_ratings")
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Fixed syntax.")
