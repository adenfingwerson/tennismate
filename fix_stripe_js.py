import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the dangling stripe logic
old_regex = r'    const stripeBtn = document\.getElementById\('stripeCheckoutBtn'\);\s*if \(stripeBtn\) \{\s*stripeBtn\.href = coach\.stripeCoaching \|\| "https://buy\.stripe\.com/7sY7sD22CeHQdWs9zhaZi01";\s*stripeBtn\.innerText = `1-Hour Lesson \(\$` \+ \(coach\.coachingPrice \|\| '25'\) \+ `\)`\s*\}\)`.*?}?'

new_js = """    const stripeBtn = document.getElementById('stripeCheckoutBtn');
    if (stripeBtn) {
      stripeBtn.href = coach.stripeCoaching || 'https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01';
      stripeBtn.innerText = `1-Hour Lesson ($` + (coach.coachingPrice || '25') + `)`;
    }"""

content = re.sub(old_regex, new_js, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
