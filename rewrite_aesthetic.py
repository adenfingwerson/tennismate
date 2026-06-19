import re

# UPDATE INDEX.HTML
with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<section class="raqgen-section".*?</section>', re.DOTALL)

new_section = """<section class="raqgen-section" style="padding: 100px 20px; background-color: var(--bg); border-top: 4px solid var(--border-dark);">
        <div class="container" style="max-width: 1000px;">
            <div style="text-align: center; margin-bottom: 60px;">
                <!-- 2026 Academic / Brutalist Logo -->
                <div style="display: inline-block; border: 4px solid var(--border-dark); padding: 12px 24px; margin-bottom: 32px; position: relative; background: #fff; box-shadow: 8px 8px 0px var(--accent);">
                    <div style="position: absolute; top: -10px; left: -10px; width: 20px; height: 20px; background: var(--border-dark);"></div>
                    <svg width="240" height="40" viewBox="0 0 240 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <text x="0" y="32" font-family="Inter, sans-serif" font-weight="900" font-size="40" fill="#000" letter-spacing="-2">RaQGeN</text>
                        <rect x="155" y="4" width="30" height="30" fill="#ccff00" stroke="#000" stroke-width="4"/>
                        <text x="162" y="26" font-family="Inter, sans-serif" font-weight="900" font-size="16" fill="#000">OS</text>
                        <text x="195" y="30" font-family="Inter, sans-serif" font-weight="900" font-size="16" fill="#000" letter-spacing="1">V.2</text>
                    </svg>
                </div>
                <h2 style="font-size: clamp(2.5rem, 6vw, 4rem); font-weight: 900; line-height: 1; margin-bottom: 20px; text-transform: uppercase;">The Master Equation.</h2>
                <p style="color: var(--text-muted); font-size: 1.2rem; max-width: 650px; margin: 0 auto; font-weight: 500;">
                    A.I. Personalized Racket Recommendation Engine. Powered by OSINT, TF-IDF Scraping, and the Mahalanobis Distance Equation.
                </p>
            </div>

            <div style="border: 4px solid var(--border-dark); padding: 40px; background: #fff; box-shadow: 16px 16px 0px var(--border-dark);">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 40px; margin-bottom: 40px;">
                    
                    <!-- Bio Input -->
                    <div>
                        <h4 style="font-size: 1.1rem; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; border-bottom: 4px solid var(--border-dark); padding-bottom: 8px; margin-bottom: 24px;">Biomechanics</h4>
                        <div style="margin-bottom: 20px;">
                            <label style="display: block; font-size: 0.9rem; font-weight: 900; margin-bottom: 8px;">Height (Inches)</label>
                            <input type="number" id="idx-raq-height" placeholder="72" class="tm-input" style="width: 100%; border: 2px solid var(--border-dark); background: #f4f4f4; padding: 14px; font-weight: 700; font-size: 1.1rem;">
                        </div>
                        <div style="margin-bottom: 20px;">
                            <label style="display: block; font-size: 0.9rem; font-weight: 900; margin-bottom: 8px;">Weight (lbs)</label>
                            <input type="number" id="idx-raq-weight" placeholder="165" class="tm-input" style="width: 100%; border: 2px solid var(--border-dark); background: #f4f4f4; padding: 14px; font-weight: 700; font-size: 1.1rem;">
                        </div>
                        <div>
                            <label style="display: block; font-size: 0.9rem; font-weight: 900; margin-bottom: 8px;">Wingspan (Inches)</label>
                            <input type="number" id="idx-raq-wingspan" placeholder="74" class="tm-input" style="width: 100%; border: 2px solid var(--border-dark); background: #f4f4f4; padding: 14px; font-weight: 700; font-size: 1.1rem;">
                        </div>
                    </div>

                    <!-- Dynamics Input -->
                    <div>
                        <h4 style="font-size: 1.1rem; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; border-bottom: 4px solid var(--border-dark); padding-bottom: 8px; margin-bottom: 24px;">Dynamics</h4>
                        <div style="margin-bottom: 20px;">
                            <label style="display: block; font-size: 0.9rem; font-weight: 900; margin-bottom: 8px;">Forehand Grip</label>
                            <select id="idx-raq-grip" style="width: 100%; border: 2px solid var(--border-dark); background: #f4f4f4; padding: 14px; font-weight: 700; font-size: 1.1rem; font-family: 'Inter', sans-serif;">
                                <option>Eastern</option>
                                <option selected>Semi-Western</option>
                                <option>Western</option>
                            </select>
                        </div>
                        <div style="margin-bottom: 20px;">
                            <label style="display: block; font-size: 0.9rem; font-weight: 900; margin-bottom: 8px;">Backhand</label>
                            <select id="idx-raq-bh" style="width: 100%; border: 2px solid var(--border-dark); background: #f4f4f4; padding: 14px; font-weight: 700; font-size: 1.1rem; font-family: 'Inter', sans-serif;">
                                <option selected>Two-Handed</option>
                                <option>One-Handed</option>
                                <option>Slice Only</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; font-size: 0.9rem; font-weight: 900; margin-bottom: 8px;">Playstyle</label>
                            <select id="idx-raq-style" style="width: 100%; border: 2px solid var(--border-dark); background: #f4f4f4; padding: 14px; font-weight: 700; font-size: 1.1rem; font-family: 'Inter', sans-serif;">
                                <option selected>All-Court Player</option>
                                <option>Aggressive Baseliner</option>
                                <option>Counter-Puncher</option>
                                <option>Serve & Volley</option>
                            </select>
                        </div>
                    </div>
                </div>

                <div class="echo-button-wrapper" style="width: 100%; display: block;">
                    <div class="echo-ring" style="border-color: var(--border-dark);"></div>
                    <button id="btn-idx-raqgen" class="btn echo-button" style="width: 100%; font-size: 1.2rem; padding: 20px; background: var(--text); color: var(--bg); border: 2px solid var(--border-dark); font-weight: 900; letter-spacing: 2px; text-transform: uppercase; cursor: pointer;" onclick="runIndexRaqGen()">
                        Compute Optimal Frame
                    </button>
                </div>

                <!-- RESULTS CONTAINER -->
                <div id="idx-raqgen-result" style="display: none; margin-top: 60px; padding-top: 40px; border-top: 4px dashed var(--border-dark);">
                    
                    <!-- BEST MATCH -->
                    <div style="border: 4px solid var(--border-dark); padding: 30px; margin-bottom: 40px; position: relative; background: #fff;">
                        <div style="position: absolute; top: -18px; right: 20px; background: var(--accent); border: 4px solid var(--border-dark); padding: 6px 16px; font-weight: 900; letter-spacing: 1px; font-size: 1rem; box-shadow: 4px 4px 0px var(--border-dark);">100% MATCH</div>
                        
                        <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 40px;">
                            <span style="font-size: 0.9rem; font-weight: 900; text-transform: uppercase; color: var(--text-muted); letter-spacing: 2px;">Primary Recommendation</span>
                            <h4 style="font-size: clamp(2rem, 5vw, 3.5rem); margin: 0; font-weight: 900; line-height: 1; text-transform: uppercase;" id="idx-raqgen-name">--</h4>
                        </div>

                        <!-- SCORE BARS -->
                        <div style="margin-bottom: 40px;">
                            <div style="margin-bottom: 24px;">
                                <div style="display: flex; justify-content: space-between; font-size: 1rem; font-weight: 900; margin-bottom: 8px; text-transform: uppercase;">
                                    <span>Bio-Kinetic Fit</span>
                                    <span id="idx-bar-bio-val">--%</span>
                                </div>
                                <div style="width: 100%; height: 16px; background: #eee; border: 2px solid var(--border-dark);">
                                    <div id="idx-bar-bio" style="height: 100%; background: var(--text); width: 0%; transition: width 1s ease-out;"></div>
                                </div>
                            </div>
                            <div style="margin-bottom: 24px;">
                                <div style="display: flex; justify-content: space-between; font-size: 1rem; font-weight: 900; margin-bottom: 8px; text-transform: uppercase;">
                                    <span>Tactical Alignment</span>
                                    <span id="idx-bar-tac-val">--%</span>
                                </div>
                                <div style="width: 100%; height: 16px; background: #eee; border: 2px solid var(--border-dark);">
                                    <div id="idx-bar-tac" style="height: 100%; background: var(--text); width: 0%; transition: width 1s ease-out 0.2s;"></div>
                                </div>
                            </div>
                            <div>
                                <div style="display: flex; justify-content: space-between; font-size: 1rem; font-weight: 900; margin-bottom: 8px; text-transform: uppercase;">
                                    <span>Arm Safety / Fatigue</span>
                                    <span id="idx-bar-safe-val">--%</span>
                                </div>
                                <div style="width: 100%; height: 16px; background: #eee; border: 2px solid var(--border-dark);">
                                    <div id="idx-bar-safe" style="height: 100%; background: var(--accent); width: 0%; transition: width 1s ease-out 0.4s;"></div>
                                </div>
                            </div>
                        </div>

                        <!-- SPECS -->
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap: 20px; border-top: 4px solid var(--border-dark); padding-top: 30px;">
                            <div><span style="display: block; font-size: 0.85rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; margin-bottom: 4px;">Mass</span> <span style="font-weight: 900; font-size: 1.8rem;" id="idx-raqgen-weight">--</span></div>
                            <div><span style="display: block; font-size: 0.85rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; margin-bottom: 4px;">Swingweight</span> <span style="font-weight: 900; font-size: 1.8rem;" id="idx-raqgen-sw">--</span></div>
                            <div><span style="display: block; font-size: 0.85rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; margin-bottom: 4px;">Stiffness (RA)</span> <span style="font-weight: 900; font-size: 1.8rem;" id="idx-raqgen-ra">--</span></div>
                            <div><span style="display: block; font-size: 0.85rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; margin-bottom: 4px;">Pattern</span> <span style="font-weight: 900; font-size: 1.8rem;" id="idx-raqgen-pattern">--</span></div>
                        </div>
                    </div>

                    <!-- RUNNERS UP -->
                    <h5 style="font-size: 1.1rem; font-weight: 900; text-transform: uppercase; margin-bottom: 20px;">Mathematical Alternatives</h5>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
                        <div style="border: 2px solid var(--border-dark); padding: 24px; display: flex; justify-content: space-between; align-items: center; background: #f4f4f4;">
                            <span style="font-weight: 900; font-size: 1.2rem; text-transform: uppercase;" id="idx-ru1-name">--</span>
                            <span style="background: var(--text); color: var(--bg); padding: 6px 12px; font-weight: 900; font-size: 1.1rem;" id="idx-ru1-score">--%</span>
                        </div>
                        <div style="border: 2px solid var(--border-dark); padding: 24px; display: flex; justify-content: space-between; align-items: center; background: #f4f4f4;">
                            <span style="font-weight: 900; font-size: 1.2rem; text-transform: uppercase;" id="idx-ru2-name">--</span>
                            <span style="background: var(--text); color: var(--bg); padding: 6px 12px; font-weight: 900; font-size: 1.1rem;" id="idx-ru2-score">--%</span>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>"""

content = pattern.sub(new_section, content)

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# UPDATE PROFILE.HTML
with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'r', encoding='utf-8') as f:
    content = f.read()

profile_pattern = re.compile(r'<div id="tab-tools" class="tab-content">.*?</div>\s*</div>\s*</div>', re.DOTALL)

new_profile_section = """<div id="tab-tools" class="tab-content">
        <div class="tactical-card" style="background: #fff; color: var(--text); margin-bottom: 24px; border: 4px solid var(--border-dark); box-shadow: 12px 12px 0px var(--border-dark);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 32px;">
                <!-- 2026 Academic / Brutalist Logo -->
                <div style="display: inline-block; border: 3px solid var(--border-dark); padding: 8px 16px; position: relative; background: #fff; box-shadow: 4px 4px 0px var(--accent);">
                    <div style="position: absolute; top: -6px; left: -6px; width: 12px; height: 12px; background: var(--border-dark);"></div>
                    <svg width="180" height="30" viewBox="0 0 240 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <text x="0" y="32" font-family="Inter, sans-serif" font-weight="900" font-size="40" fill="#000" letter-spacing="-2">RaQGeN</text>
                        <rect x="155" y="4" width="30" height="30" fill="#ccff00" stroke="#000" stroke-width="4"/>
                        <text x="162" y="26" font-family="Inter, sans-serif" font-weight="900" font-size="16" fill="#000">OS</text>
                        <text x="195" y="30" font-family="Inter, sans-serif" font-weight="900" font-size="16" fill="#000" letter-spacing="1">V.2</text>
                    </svg>
                </div>
            </div>
            
            <p style="margin-bottom: 32px; color: var(--text-muted); font-size: 1.1rem; font-weight: 500;">
                A.I. Personalized Racket Recommendation Engine. Powered by OSINT, TF-IDF Scraping, and the Mahalanobis Distance Equation.
            </p>
            
            <div class="grid-layout" style="margin-bottom: 32px; gap: 24px;">
                <div class="data-card" style="background: #f4f4f4; border: 2px solid var(--border-dark);">
                    <h4 style="margin-bottom: 20px; color: var(--text); font-size: 0.9rem; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; border-bottom: 2px solid var(--border-dark); padding-bottom: 8px;">BIOMECHANICS</h4>
                    <div class="stat-row" style="border-bottom: 1px solid #ddd; padding-bottom: 12px;">
                        <span style="color: var(--text-muted); font-size: 0.9rem; font-weight: 700;">Height</span>
                        <span style="color: var(--text); font-weight: 900;" id="raq-height">Auto-Linked</span>
                    </div>
                    <div class="stat-row" style="border-bottom: 1px solid #ddd; padding: 12px 0;">
                        <span style="color: var(--text-muted); font-size: 0.9rem; font-weight: 700;">Weight</span>
                        <span style="color: var(--text); font-weight: 900;" id="raq-weight">Auto-Linked</span>
                    </div>
                    <div class="stat-row" style="padding-top: 12px;">
                        <span style="color: var(--text-muted); font-size: 0.9rem; font-weight: 700;">Wingspan</span>
                        <span style="color: var(--text); font-weight: 900;" id="raq-wingspan">Auto-Linked</span>
                    </div>
                </div>
                
                <div class="data-card" style="background: #f4f4f4; border: 2px solid var(--border-dark);">
                    <h4 style="margin-bottom: 20px; color: var(--text); font-size: 0.9rem; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; border-bottom: 2px solid var(--border-dark); padding-bottom: 8px;">DYNAMICS</h4>
                    <div class="stat-row" style="border-bottom: 1px solid #ddd; padding-bottom: 12px;">
                        <span style="color: var(--text-muted); font-size: 0.9rem; font-weight: 700;">Forehand</span>
                        <span style="color: var(--text); font-weight: 900;" id="raq-grip">Auto-Linked</span>
                    </div>
                    <div class="stat-row" style="border-bottom: 1px solid #ddd; padding: 12px 0;">
                        <span style="color: var(--text-muted); font-size: 0.9rem; font-weight: 700;">Backhand</span>
                        <span style="color: var(--text); font-weight: 900;" id="raq-bh">Auto-Linked</span>
                    </div>
                    <div class="stat-row" style="padding-top: 12px;">
                        <span style="color: var(--text-muted); font-size: 0.9rem; font-weight: 700;">Playstyle</span>
                        <span style="color: var(--text); font-weight: 900;" id="raq-style">Auto-Linked</span>
                    </div>
                </div>
            </div>

            <button class="tm-btn echo-button" id="btn-raqgen" style="width: 100%; font-size: 1.1rem; padding: 20px; background: var(--text); color: var(--bg); border: 2px solid var(--border-dark); font-weight: 900; letter-spacing: 2px; text-transform: uppercase; cursor: pointer;" onclick="generateRaqGen()">
                INITIALIZE MASTER EQUATION
            </button>
            
            <!-- RESULTS CONTAINER -->
            <div id="raqgen-result" style="display: none; margin-top: 40px; padding-top: 32px; border-top: 4px dashed var(--border-dark);">
                
                <!-- BEST MATCH -->
                <div style="background: #fff; border: 4px solid var(--border-dark); padding: 24px; margin-bottom: 32px; position: relative;">
                    <div style="position: absolute; top: -14px; right: 16px; background: var(--accent); border: 2px solid var(--border-dark); padding: 4px 10px; font-weight: 900; letter-spacing: 1px; font-size: 0.8rem; box-shadow: 2px 2px 0px var(--border-dark);">100% MATCH</div>
                    
                    <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 32px;">
                        <span style="font-size: 0.8rem; font-weight: 900; text-transform: uppercase; color: var(--text-muted); letter-spacing: 2px;">Primary Recommendation</span>
                        <h4 style="font-size: clamp(1.5rem, 4vw, 2.5rem); margin: 0; font-weight: 900; line-height: 1; text-transform: uppercase;" id="raqgen-racket-name">--</h4>
                    </div>

                    <!-- SCORE BARS -->
                    <div style="margin-bottom: 32px;">
                        <div style="margin-bottom: 16px;">
                            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 900; margin-bottom: 6px; text-transform: uppercase;">
                                <span>Bio-Kinetic Fit</span>
                                <span id="bar-bio-val">--%</span>
                            </div>
                            <div style="width: 100%; height: 10px; background: #eee; border: 2px solid var(--border-dark);">
                                <div id="bar-bio" style="height: 100%; background: var(--text); width: 0%; transition: width 1s ease-out;"></div>
                            </div>
                        </div>
                        <div style="margin-bottom: 16px;">
                            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 900; margin-bottom: 6px; text-transform: uppercase;">
                                <span>Tactical Alignment</span>
                                <span id="bar-tac-val">--%</span>
                            </div>
                            <div style="width: 100%; height: 10px; background: #eee; border: 2px solid var(--border-dark);">
                                <div id="bar-tac" style="height: 100%; background: var(--text); width: 0%; transition: width 1s ease-out 0.2s;"></div>
                            </div>
                        </div>
                        <div>
                            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 900; margin-bottom: 6px; text-transform: uppercase;">
                                <span>Arm Safety / Fatigue</span>
                                <span id="bar-safe-val">--%</span>
                            </div>
                            <div style="width: 100%; height: 10px; background: #eee; border: 2px solid var(--border-dark);">
                                <div id="bar-safe" style="height: 100%; background: var(--accent); width: 0%; transition: width 1s ease-out 0.4s;"></div>
                            </div>
                        </div>
                    </div>

                    <!-- SPECS -->
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap: 16px; border-top: 2px dashed var(--border-dark); padding-top: 20px;">
                        <div><span style="display: block; font-size: 0.75rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; margin-bottom: 4px;">Mass</span> <span style="font-weight: 900; font-size: 1.4rem;" id="raqgen-weight">--</span></div>
                        <div><span style="display: block; font-size: 0.75rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; margin-bottom: 4px;">Swingweight</span> <span style="font-weight: 900; font-size: 1.4rem;" id="raqgen-sw">--</span></div>
                        <div><span style="display: block; font-size: 0.75rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; margin-bottom: 4px;">Stiffness</span> <span style="font-weight: 900; font-size: 1.4rem;" id="raqgen-ra">--</span></div>
                        <div><span style="display: block; font-size: 0.75rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; margin-bottom: 4px;">Pattern</span> <span style="font-weight: 900; font-size: 1.4rem;" id="raqgen-pattern">--</span></div>
                    </div>
                </div>

                <!-- RUNNERS UP -->
                <h5 style="font-size: 1rem; font-weight: 900; text-transform: uppercase; margin-bottom: 16px;">Mathematical Alternatives</h5>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px;">
                    <div style="border: 2px solid var(--border-dark); padding: 16px; display: flex; justify-content: space-between; align-items: center; background: #f4f4f4;">
                        <span style="font-weight: 900; font-size: 1.1rem; text-transform: uppercase;" id="ru1-name">--</span>
                        <span style="background: var(--text); color: var(--bg); padding: 4px 8px; font-weight: 900;" id="ru1-score">--%</span>
                    </div>
                    <div style="border: 2px solid var(--border-dark); padding: 16px; display: flex; justify-content: space-between; align-items: center; background: #f4f4f4;">
                        <span style="font-weight: 900; font-size: 1.1rem; text-transform: uppercase;" id="ru2-name">--</span>
                        <span style="background: var(--text); color: var(--bg); padding: 4px 8px; font-weight: 900;" id="ru2-score">--%</span>
                    </div>
                </div>

            </div>
        </div>
    </div>
</div>
</div>"""

content = profile_pattern.sub(new_profile_section, content)

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Aesthetic update complete.")
