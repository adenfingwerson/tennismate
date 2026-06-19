with open('index.html', 'r') as f:
    content = f.read()

# Replace all cal.com links with the known stripe link
new_content = content.replace('https://cal.com/tennis-t-mate-hcmfls', 'https://buy.stripe.com/7sY7sD22CeHQdWs9zhaZi01')

with open('index.html', 'w') as f:
    f.write(new_content)
