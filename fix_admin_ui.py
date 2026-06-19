import re

with open('admin.html', 'r') as f:
    html = f.read()

# Fix the AI output rendering in admin.html so the coach can preview the generated JSON cleanly
old_js = """
                if(data.success) {
                    const out = document.getElementById('ai-output');
                    out.style.display = 'block';
                    out.innerText = data.ai_plan;
                }
"""

new_js = """
                if(data.success) {
                    const out = document.getElementById('ai-output');
                    out.style.display = 'block';
                    out.innerHTML = `<strong>FOCUS:</strong> ${data.ai_plan.core_focus}<br><br><strong>CUES:</strong><br>- ${data.ai_plan.mechanical_cues.join('<br>- ')}<br><br><strong>RULE:</strong> ${data.ai_plan.tactical_rule}`;
                }
"""

html = html.replace(old_js.strip(), new_js.strip())

with open('admin.html', 'w') as f:
    f.write(html)

print("Admin HTML JS patched.")