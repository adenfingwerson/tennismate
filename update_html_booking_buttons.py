import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace book buttons opening modal with link to booking.html
# e.g. <a href="#" onclick="openModal(event)" class="...">Book Now</a>
new_content = re.sub(r'href="#" onclick="openModal\(event\)"', r'href="/booking.html"', content)

with open('index.html', 'w') as f:
    f.write(new_content)
