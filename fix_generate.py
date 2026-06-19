import re

with open('functions/api/admin/generate.js', 'r') as f:
    js = f.read()

# Fix the newline issue
js = js.replace('join("\\\\n\\\\n");', 'join("\\n\\n");')
js = js.replace('join("\\n\\n");', 'join("\\\\n\\\\n");')

with open('functions/api/admin/generate.js', 'w') as f:
    f.write(js)
