import re

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

raqgen_section = """
    <section class="raqgen-section" style="padding: 100px 20px; background-color: #000; color: #fff; border-top: 1px solid #222;">
        <div class="container" style="max-width: 1000px;">
            <div style="text-align: center; margin-bottom: 50px;">
                <div style="display: inline-flex; align-items: center; justify-content: center; gap: 16px; margin-bottom: 24px;">
                    <!-- Custom RaQGeN Logo SVG -->
                    <svg width="240" height="50" viewBox="0 0 200 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M10 5H30C38.2843 5 45 11.7157 45 20C45 23.4797 43.8166 26.6833 41.8028 29.2155L50 35H35L29 28H18V35H10V5ZM18 13V21H30C32.2091 21 34 19.2091 34 17C34 14.7909 32.2091 13 30 13H18Z" fill="#00ffcc"/>
                        <path d="M55 25C55 19.4772 59.4772 15 65 15H75V35H65C59.4772 35 55 30.5228 55 25ZM63 25C63 26.1046 63.8954 27 65 27H67V23H65C63.8954 23 63 23.8954 63 25Z" fill="#ffffff"/>
                        <path d="M85 20C85 11.7157 91.7157 5 100 5C108.284 5 115 11.7157 115 20C115 28.2843 108.284 35 100 35C91.7157 35 85 28.2843 85 20ZM93 20C93 23.866 96.134 27 100 27C103.866 27 107 23.866 107 20C107 16.134 103.866 13 100 13C96.134 13 93 16.134 93 20Z" fill="#00ffcc"/>
                        <path d="M100 13V5" stroke="#00ffcc" stroke-width="2"/>
                        <path d="M100 35V27" stroke="#00ffcc" stroke-width="2"/>
                        <path d="M85 20H93" stroke="#00ffcc" stroke-width="2"/>
                        <path d="M115 20H107" stroke="#00ffcc" stroke-width="2"/>
                        <path d="M109 29L120 40" stroke="#00ffcc" stroke-width="3" stroke-linecap="square"/>
                        <path d="M125 20C125 11.7157 131.716 5 140 5H150V13H140C136.134 13 133 16.134 133 20C133 23.866 136.134 27 140 27H142V20H150V35H140C131.716 35 125 28.2843 125 20Z" fill="#ffffff"/>
                        <path d="M155 25C155 19.4772 159.477 15 165 15H175V23H163C163 24.1046 163.895 25 165 25H175V35H165C159.477 35 155 30.5228 155 25Z" fill="#ffffff"/>
                        <path d="M180 35V5H188L195 20V5H200V35H192L185 20V35H180Z" fill="#00ffcc"/>
                    </svg>
                    <span style="font-size: 0.9rem; background: #00ffcc; color: #000; padding: 4px 10px; border-radius: 4px; font-weight: 900; letter-spacing: 1px;">PRO</span>
                </div>
                <h2 style="font-size: clamp(2rem, 4vw, 3rem); font-weight: 900; color: #fff; margin-bottom: 16px;">The Master Equation.</h2>
                <p style="color: #aaa; font-size: 1.1rem; max-width: 600px; margin: 0 auto;">
                    A.I. Personalized Racket Recommendation Engine. Powered by OSINT, TF-IDF Scraping, and the Mahalanobis Distance Equation. Find your mathematically perfect frame.
                </p>
            </div>

            <div style="background: #111; border: 1px solid #333; border-radius: 12px; padding: 32px; box-shadow: 0 10px 40px rgba(0,0,0,0.8);">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px; margin-bottom: 32px;">
                    
                    <!-- Bio Input -->
                    <div>
                        <h4 style="color: #00ffcc; font-size: 0.9rem; letter-spacing: 1px; margin-bottom: 16px;">BIOMECHANICS</h4>
                        
                        <div style="margin-bottom: 16px;">
                            <label style="display: block; font-size: 0.85rem; color: #888; margin-bottom: 4px;">Height (Inches)</label>
                            <input type="number" id="idx-raq-height" placeholder="e.g. 72" style="width: 100%; padding: 12px; background: #000; border: 1px solid #333; color: #fff; border-radius: 6px; font-size: 1rem;">
                        </div>
                        <div style="margin-bottom: 16px;">
                            <label style="display: block; font-size: 0.85rem; color: #888; margin-bottom: 4px;">Weight (lbs)</label>
                            <input type="number" id="idx-raq-weight" placeholder="e.g. 165" style="width: 100%; padding: 12px; background: #000; border: 1px solid #333; color: #fff; border-radius: 6px; font-size: 1rem;">
                        </div>
                        <div>
                            <label style="display: block; font-size: 0.85rem; color: #888; margin-bottom: 4px;">Wingspan (Inches)</label>
                            <input type="number" id="idx-raq-wingspan" placeholder="e.g. 74" style="width: 100%; padding: 12px; background: #000; border: 1px solid #333; color: #fff; border-radius: 6px; font-size: 1rem;">
                        </div>
                    </div>

                    <!-- Dynamics Input -->
                    <div>
                        <h4 style="color: #00ffcc; font-size: 0.9rem; letter-spacing: 1px; margin-bottom: 16px;">DYNAMICS</h4>
                        
                        <div style="margin-bottom: 16px;">
                            <label style="display: block; font-size: 0.85rem; color: #888; margin-bottom: 4px;">Forehand Grip</label>
                            <select id="idx-raq-grip" style="width: 100%; padding: 12px; background: #000; border: 1px solid #333; color: #fff; border-radius: 6px; font-size: 1rem; appearance: none;">
                                <option>Eastern</option>
                                <option selected>Semi-Western</option>
                                <option>Western</option>
                            </select>
                        </div>
                        <div style="margin-bottom: 16px;">
                            <label style="display: block; font-size: 0.85rem; color: #888; margin-bottom: 4px;">Backhand</label>
                            <select id="idx-raq-bh" style="width: 100%; padding: 12px; background: #000; border: 1px solid #333; color: #fff; border-radius: 6px; font-size: 1rem; appearance: none;">
                                <option selected>Two-Handed</option>
                                <option>One-Handed</option>
                                <option>Slice Only</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; font-size: 0.85rem; color: #888; margin-bottom: 4px;">Playstyle</label>
                            <select id="idx-raq-style" style="width: 100%; padding: 12px; background: #000; border: 1px solid #333; color: #fff; border-radius: 6px; font-size: 1rem; appearance: none;">
                                <option selected>All-Court Player</option>
                                <option>Aggressive Baseliner</option>
                                <option>Counter-Puncher</option>
                                <option>Serve & Volley</option>
                            </select>
                        </div>
                    </div>
                </div>

                <button class="btn" id="btn-idx-raqgen" style="width: 100%; font-size: 1.1rem; padding: 20px; background: linear-gradient(90deg, #00ffcc 0%, #00b3ff 100%); color: #000; border: none; font-weight: 900; letter-spacing: 1px; transition: opacity 0.2s; border-radius: 8px;" onclick="runIndexRaqGen()">
                    INITIALIZE MASTER EQUATION
                </button>

                <!-- RESULTS CONTAINER -->
                <div id="idx-raqgen-result" style="display: none; margin-top: 40px; padding-top: 32px; border-top: 1px solid #333;">
                    
                    <!-- BEST MATCH -->
                    <div style="background: #1a1a1a; border: 1px solid #00ffcc; border-radius: 8px; padding: 24px; margin-bottom: 24px; position: relative; overflow: hidden;">
                        <div style="position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: #00ffcc;"></div>
                        
                        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px;">
                            <div>
                                <span style="font-size: 0.75rem; color: #00ffcc; font-weight: 900; letter-spacing: 2px;">OPTIMAL FRAME MATRIX</span>
                                <h4 style="font-size: clamp(1.4rem, 3vw, 2rem); margin: 4px 0 0 0; color: #fff;" id="idx-raqgen-name">--</h4>
                            </div>
                            <div style="text-align: right;">
                                <span style="font-size: 0.75rem; color: #888; font-weight: 700; letter-spacing: 1px;">MATCH SCORE</span>
                                <div style="font-size: clamp(1.8rem, 4vw, 2.5rem); font-weight: 900; color: #00ffcc; line-height: 1;" id="idx-raqgen-score">--%</div>
                            </div>
                        </div>

                        <!-- SCORE BARS -->
                        <div style="margin-bottom: 24px;">
                            <div style="margin-bottom: 14px;">
                                <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 6px; color: #ccc;">
                                    <span>Bio-Kinetic Fit</span>
                                    <span id="idx-bar-bio-val">--%</span>
                                </div>
                                <div style="width: 100%; height: 8px; background: #333; border-radius: 4px; overflow: hidden;">
                                    <div id="idx-bar-bio" style="height: 100%; background: #00ffcc; width: 0%; transition: width 1s ease-out;"></div>
                                </div>
                            </div>
                            <div style="margin-bottom: 14px;">
                                <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 6px; color: #ccc;">
                                    <span>Tactical Alignment</span>
                                    <span id="idx-bar-tac-val">--%</span>
                                </div>
                                <div style="width: 100%; height: 8px; background: #333; border-radius: 4px; overflow: hidden;">
                                    <div id="idx-bar-tac" style="height: 100%; background: #00b3ff; width: 0%; transition: width 1s ease-out 0.2s;"></div>
                                </div>
                            </div>
                            <div>
                                <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 6px; color: #ccc;">
                                    <span>Arm Safety / Fatigue</span>
                                    <span id="idx-bar-safe-val">--%</span>
                                </div>
                                <div style="width: 100%; height: 8px; background: #333; border-radius: 4px; overflow: hidden;">
                                    <div id="idx-bar-safe" style="height: 100%; background: #ff00cc; width: 0%; transition: width 1s ease-out 0.4s;"></div>
                                </div>
                            </div>
                        </div>

                        <!-- SPECS -->
                        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; font-size: 0.9rem; border-top: 1px solid #333; padding-top: 20px;">
                            <div><span style="color: #666; display: block; font-size: 0.7rem; text-transform: uppercase;">Mass</span> <span style="color: #fff; font-weight: 700; font-size: 1.1rem;" id="idx-raqgen-weight">--</span></div>
                            <div><span style="color: #666; display: block; font-size: 0.7rem; text-transform: uppercase;">Swingweight</span> <span style="color: #fff; font-weight: 700; font-size: 1.1rem;" id="idx-raqgen-sw">--</span></div>
                            <div><span style="color: #666; display: block; font-size: 0.7rem; text-transform: uppercase;">Stiffness (RA)</span> <span style="color: #fff; font-weight: 700; font-size: 1.1rem;" id="idx-raqgen-ra">--</span></div>
                            <div><span style="color: #666; display: block; font-size: 0.7rem; text-transform: uppercase;">Pattern</span> <span style="color: #fff; font-weight: 700; font-size: 1.1rem;" id="idx-raqgen-pattern">--</span></div>
                        </div>
                    </div>

                    <!-- RUNNERS UP -->
                    <h5 style="font-size: 0.85rem; color: #888; margin-bottom: 16px; letter-spacing: 1px;">ALTERNATIVES</h5>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                        <div style="background: #111; border: 1px solid #333; border-radius: 6px; padding: 16px; display: flex; justify-content: space-between; align-items: center;">
                            <span style="color: #ccc; font-size: 1rem; font-weight: 500;" id="idx-ru1-name">--</span>
                            <span style="color: #00ffcc; font-weight: 900; font-size: 1.1rem;" id="idx-ru1-score">--%</span>
                        </div>
                        <div style="background: #111; border: 1px solid #333; border-radius: 6px; padding: 16px; display: flex; justify-content: space-between; align-items: center;">
                            <span style="color: #ccc; font-size: 1rem; font-weight: 500;" id="idx-ru2-name">--</span>
                            <span style="color: #00ffcc; font-weight: 900; font-size: 1.1rem;" id="idx-ru2-score">--%</span>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>
"""

content = content.replace('<section class="second-cta"', raqgen_section + '\n\n<section class="second-cta"')

js_script = """
<script>
    async function runIndexRaqGen() {
        const btn = document.getElementById('btn-idx-raqgen');
        const originalText = btn.innerText;
        btn.innerText = "CALCULATING MATRICES...";
        btn.style.opacity = "0.7";
        
        let heightStr = document.getElementById('idx-raq-height').value || '72';
        let weightStr = document.getElementById('idx-raq-weight').value || '160';
        let wingspanStr = document.getElementById('idx-raq-wingspan').value || '72';
        let gripVal = document.getElementById('idx-raq-grip').value || 'Semi-Western';
        let bhVal = document.getElementById('idx-raq-bh').value || 'Two-Handed';
        let styleVal = document.getElementById('idx-raq-style').value || 'All-Court Player';

        try {
            const res = await fetch('/api/raqgen', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    height: heightStr,
                    weight: weightStr,
                    wingspan: wingspanStr,
                    style: styleVal,
                    grip: gripVal,
                    bh: bhVal
                })
            });
            
            const data = await res.json();
            
            if (data.success) {
                document.getElementById('idx-raqgen-result').style.display = 'block';
                
                // Best Match
                document.getElementById('idx-raqgen-name').innerText = data.best_match.name;
                document.getElementById('idx-raqgen-score').innerText = data.best_match.score.toFixed(1) + "%";
                document.getElementById('idx-raqgen-weight').innerText = data.best_match.specs.weight + "g";
                document.getElementById('idx-raqgen-sw').innerText = data.best_match.specs.sw;
                document.getElementById('idx-raqgen-ra').innerText = data.best_match.specs.ra + ' (Dyn: ' + data.best_match.specs.dynamic + 'Hz)';
                document.getElementById('idx-raqgen-pattern').innerText = data.best_match.specs.pattern;

                // Animate Bars
                setTimeout(() => {
                    document.getElementById('idx-bar-bio').style.width = data.best_match.bio_score + "%";
                    document.getElementById('idx-bar-bio-val').innerText = data.best_match.bio_score.toFixed(0) + "%";
                    
                    document.getElementById('idx-bar-tac').style.width = data.best_match.tac_score + "%";
                    document.getElementById('idx-bar-tac-val').innerText = data.best_match.tac_score.toFixed(0) + "%";
                    
                    document.getElementById('idx-bar-safe').style.width = data.best_match.safe_score + "%";
                    document.getElementById('idx-bar-safe-val').innerText = data.best_match.safe_score.toFixed(0) + "%";
                }, 100);

                // Runners Up
                document.getElementById('idx-ru1-name').innerText = data.runner_up_1.name;
                document.getElementById('idx-ru1-score').innerText = data.runner_up_1.score.toFixed(1) + "%";
                
                document.getElementById('idx-ru2-name').innerText = data.runner_up_2.name;
                document.getElementById('idx-ru2-score').innerText = data.runner_up_2.score.toFixed(1) + "%";

            } else {
                alert("RaQGeN computation failed.");
            }
        } catch(e) {
            console.error(e);
            alert("Error connecting to RaQGeN Matrix Engine.");
        } finally {
            btn.innerText = originalText;
            btn.style.opacity = "1";
        }
    }
</script>
"""

content = content.replace('</body>', js_script + '\n</body>')

with open('/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected RaQGeN into index.html")
