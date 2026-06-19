with open('functions/api/book.js', 'r') as f:
    js = f.read()

# Fix newline literals
js = js.replace('"\\nPhone: "', '"\\\\nPhone: "')
js = js.replace('"\\nLocation: "', '"\\\\nLocation: "')
js = js.replace('"\\nTime: "', '"\\\\nTime: "')

# Also fix multiline strings if present
js = js.replace('body: "Name: " + name + "\\nPhone: " + phone + "\\nLocation: " + location + "\\nTime: " + preferred_time', 'body: "Name: " + name + "\\\\nPhone: " + phone + "\\\\nLocation: " + location + "\\\\nTime: " + preferred_time')

with open('functions/api/book.js', 'w') as f:
    f.write(js)
