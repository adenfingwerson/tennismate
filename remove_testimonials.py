import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove the testimonials section
new_content = re.sub(r'<section class="testimonials">.*?</section>', '', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(new_content)

