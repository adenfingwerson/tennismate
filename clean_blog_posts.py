import glob
import re

email_capture_html = """
        <div class="cta-box" style="margin-top: 60px; border: 1px solid var(--border-dark); padding: 0;">
            <div style="background-color: var(--text); color: var(--bg); padding: 32px;">
                <h3 style="color: var(--bg); margin-bottom: 12px; font-size: 1.5rem;">Join the Local Roster</h3>
                <p style="color: #ccc; margin-bottom: 24px; font-size: 1rem;">Drop your email to unlock full access to the Tennis T-Mate journal, exclusive local coaching tips, and priority booking in Hastings & Holdrege.</p>
                <form id="subscribe-form" style="display: flex; gap: 12px; flex-wrap: wrap;">
                    <input type="email" id="email-input" placeholder="Enter your email address" required style="flex: 1; min-width: 200px; padding: 12px 16px; border: 1px solid var(--bg); background: var(--text); color: var(--bg); font-family: inherit;">
                    <button type="submit" id="submit-btn" style="padding: 12px 24px; border: none; background: var(--bg); color: var(--text); font-weight: 700; cursor: pointer; text-transform: uppercase;">Get Access</button>
                </form>
                <p id="form-message" style="margin-top: 12px; font-size: 0.9rem; display: none;"></p>
            </div>
            <div style="padding: 32px; background: var(--bg); color: var(--text);">
                <h3 style="font-size: 1.25rem; margin-bottom: 16px; text-transform: uppercase;">What's in my bag (Coach Aden)</h3>
                <ul style="list-style: none; padding: 0; margin: 0;">
                    <li style="padding-bottom: 12px; border-bottom: 1px solid var(--border); margin-bottom: 12px;">
                        <strong style="display: block; text-transform: uppercase;">Head Gravity Tour 98</strong>
                        <span style="color: var(--text-muted); font-size: 0.9rem;">Current Racket</span>
                    </li>
                    <li style="padding-bottom: 12px; border-bottom: 1px solid var(--border); margin-bottom: 12px;">
                        <strong style="display: block; text-transform: uppercase;">Confidential Mains / Mach 10 Crosses</strong>
                        <span style="color: var(--text-muted); font-size: 0.9rem;">String Setup (Solinco)</span>
                    </li>
                    <li>
                        <strong style="display: block; text-transform: uppercase;">Solinco Overgrip</strong>
                        <span style="color: var(--text-muted); font-size: 0.9rem;">Grip</span>
                    </li>
                </ul>
            </div>
        </div>
        <script>
          document.getElementById('subscribe-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const emailInput = document.getElementById('email-input');
            const submitBtn = document.getElementById('submit-btn');
            const messageEl = document.getElementById('form-message');
            
            const email = emailInput.value;
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.7';
            submitBtn.innerText = 'Subscribing...';
            
            try {
              // Simulated API call or you can plug in your real endpoint here
              setTimeout(() => {
                  messageEl.style.display = 'block';
                  messageEl.style.color = 'var(--bg)';
                  messageEl.innerText = 'You are on the list!';
                  emailInput.value = '';
                  submitBtn.disabled = false;
                  submitBtn.style.opacity = '1';
                  submitBtn.innerText = 'Get Access';
              }, 1000);
            } catch (err) {
              messageEl.style.display = 'block';
              messageEl.style.color = '#ff4444';
              messageEl.innerText = 'Network error. Try again.';
            }
          });
        </script>
"""

for filepath in glob.glob('/Users/adeningwerson/Desktop/Tennis-Landing-Page/blog/*.html'):
    if 'index.html' in filepath:
        continue # Skip the index
        
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Remove the old affiliate box entirely
    content = re.sub(r'<div class="affiliate-box">.*?</div>', '', content, flags=re.DOTALL)
    
    # Replace the old cta-box block with the new email capture + gear block
    content = re.sub(r'<div class="cta-box">.*?</div>\s*</article>', email_capture_html + '\n      </article>', content, flags=re.DOTALL)
    
    # It might be missing the </article> in the regex if nested divs. Let's do a more robust replacement.
    # The CTA block starts with <div class="cta-box"> and goes until </article>
    content = re.sub(r'<div class="cta-box">.*?(?=</article>)', email_capture_html, content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Cleaned {filepath}")
