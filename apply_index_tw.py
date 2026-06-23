import re

filepath = '/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html'

with open(filepath, 'r') as f:
    content = f.read()

tw_dom = """
                    <!-- TW METRICS -->
                    <div style="margin-top: 32px; border-top: 2px dashed var(--border-dark); padding-top: 24px; margin-bottom: 32px;">
                        <span style="font-size: 0.8rem; font-weight: 900; text-transform: uppercase; color: var(--text-muted); letter-spacing: 2px; display: block; margin-bottom: 16px;">1-100 Performance Metrics</span>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 16px;">
                            <div style="background: #f4f4f4; padding: 12px; border: 2px solid var(--border-dark);">
                                <span style="font-size: 0.7rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; display: block; margin-bottom: 4px;">Overall</span>
                                <span style="font-weight: 900; font-size: 1.2rem;" id="idx-tw-overall">--</span>
                            </div>
                            <div style="background: #f4f4f4; padding: 12px; border: 2px solid var(--border-dark);">
                                <span style="font-size: 0.7rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; display: block; margin-bottom: 4px;">Power</span>
                                <span style="font-weight: 900; font-size: 1.2rem;" id="idx-tw-power">--</span>
                            </div>
                            <div style="background: #f4f4f4; padding: 12px; border: 2px solid var(--border-dark);">
                                <span style="font-size: 0.7rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; display: block; margin-bottom: 4px;">Control</span>
                                <span style="font-weight: 900; font-size: 1.2rem;" id="idx-tw-control">--</span>
                            </div>
                            <div style="background: #f4f4f4; padding: 12px; border: 2px solid var(--border-dark);">
                                <span style="font-size: 0.7rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; display: block; margin-bottom: 4px;">Maneuverability</span>
                                <span style="font-weight: 900; font-size: 1.2rem;" id="idx-tw-maneuver">--</span>
                            </div>
                            <div style="background: #f4f4f4; padding: 12px; border: 2px solid var(--border-dark);">
                                <span style="font-size: 0.7rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; display: block; margin-bottom: 4px;">Stability</span>
                                <span style="font-weight: 900; font-size: 1.2rem;" id="idx-tw-stability">--</span>
                            </div>
                            <div style="background: #f4f4f4; padding: 12px; border: 2px solid var(--border-dark);">
                                <span style="font-size: 0.7rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; display: block; margin-bottom: 4px;">Comfort</span>
                                <span style="font-weight: 900; font-size: 1.2rem;" id="idx-tw-comfort">--</span>
                            </div>
                            <div style="background: #f4f4f4; padding: 12px; border: 2px solid var(--border-dark);">
                                <span style="font-size: 0.7rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; display: block; margin-bottom: 4px;">Topspin</span>
                                <span style="font-weight: 900; font-size: 1.2rem;" id="idx-tw-topspin">--</span>
                            </div>
                            <div style="background: #f4f4f4; padding: 12px; border: 2px solid var(--border-dark);">
                                <span style="font-size: 0.7rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; display: block; margin-bottom: 4px;">Touch</span>
                                <span style="font-weight: 900; font-size: 1.2rem;" id="idx-tw-touch">--</span>
                            </div>
                            <div style="background: #f4f4f4; padding: 12px; border: 2px solid var(--border-dark);">
                                <span style="font-size: 0.7rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; display: block; margin-bottom: 4px;">Groundstrokes</span>
                                <span style="font-weight: 900; font-size: 1.2rem;" id="idx-tw-ground">--</span>
                            </div>
                            <div style="background: #f4f4f4; padding: 12px; border: 2px solid var(--border-dark);">
                                <span style="font-size: 0.7rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; display: block; margin-bottom: 4px;">Volleys</span>
                                <span style="font-weight: 900; font-size: 1.2rem;" id="idx-tw-volleys">--</span>
                            </div>
                            <div style="background: #f4f4f4; padding: 12px; border: 2px solid var(--border-dark);">
                                <span style="font-size: 0.7rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; display: block; margin-bottom: 4px;">Serves</span>
                                <span style="font-weight: 900; font-size: 1.2rem;" id="idx-tw-serves">--</span>
                            </div>
                            <div style="background: #f4f4f4; padding: 12px; border: 2px solid var(--border-dark);">
                                <span style="font-size: 0.7rem; font-weight: 900; color: var(--text-muted); text-transform: uppercase; display: block; margin-bottom: 4px;">Returns</span>
                                <span style="font-weight: 900; font-size: 1.2rem;" id="idx-tw-returns">--</span>
                            </div>
                        </div>
                    </div>
"""

if "1-100 Performance Metrics" not in content:
    content = content.replace("<!-- RUNNERS UP -->", tw_dom + "\\n                    <!-- RUNNERS UP -->")

with open(filepath, 'w') as f:
    f.write(content)
print("Updated index.html HTML")
