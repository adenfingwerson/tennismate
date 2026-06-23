import os
import re

files = ['/Users/adeningwerson/Desktop/Tennis-Landing-Page/index.html', '/Users/adeningwerson/Desktop/Tennis-Landing-Page/profile.html']

js_update = """
                safeSetText('raqgen-pattern', data.best_match.specs.pattern);

                if(data.best_match.tw_ratings) {
                    safeSetText('tw-overall', data.best_match.tw_ratings.overall);
                    safeSetText('tw-power', data.best_match.tw_ratings.power);
                    safeSetText('tw-control', data.best_match.tw_ratings.control);
                    safeSetText('tw-maneuver', data.best_match.tw_ratings.maneuverability);
                    safeSetText('tw-stability', data.best_match.tw_ratings.stability);
                    safeSetText('tw-comfort', data.best_match.tw_ratings.comfort);
                    safeSetText('tw-topspin', data.best_match.tw_ratings.topspin);
                    safeSetText('tw-touch', data.best_match.tw_ratings.touch);
                    safeSetText('tw-ground', data.best_match.tw_ratings.groundstrokes);
                    safeSetText('tw-volleys', data.best_match.tw_ratings.volleys);
                    safeSetText('tw-serves', data.best_match.tw_ratings.serves);
                    safeSetText('tw-returns', data.best_match.tw_ratings.returns);
                }
"""

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    if "data.best_match.tw_ratings" not in content:
        content = content.replace("safeSetText('raqgen-pattern', data.best_match.specs.pattern);", js_update)
        with open(filepath, 'w') as f:
            f.write(content)

print("Applied JS update!")
