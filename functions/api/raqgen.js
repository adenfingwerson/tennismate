export async function onRequestPost(context) {
    try {
        const p = await context.request.json();

        // Ensure we have fallbacks
        const height_in = parseFloat(p.height) || 72; // default 6'0"
        const weight_lbs = parseFloat(p.weight) || 160; 
        const wingspan_in = parseFloat(p.wingspan) || 72;
        const grip = p.grip || "Semi-Western";
        const style = p.style || "All-Court Player";
        const bh = p.bh || "Two-Handed";

        // Convert to metrics
        const height_cm = height_in * 2.54;
        const wingspan_cm = wingspan_in * 2.54;
        const weight_kg = weight_lbs * 0.453592;
        const gender_scalar = 1.0; // Assuming baseline for now
        const injury_history = 0.2; // Baseline

        // THE RACKET DATABASE (Strung Specs) - Expanded slightly
        const rackets = [
            {name: "Babolat Pure Drive", mass: 318, SW: 320, RA: 71, Hz: 155, TW: 14.5, headsize: 100, mains: 16, crosses: 19},
            {name: "Wilson Pro Staff 97", mass: 330, SW: 320, RA: 65, Hz: 135, TW: 13.8, headsize: 97,  mains: 16, crosses: 19},
            {name: "Wilson Blade 98 (18x20)", mass: 321,SW: 327, RA: 62, Hz: 130, TW: 14.2, headsize: 98,  mains: 18, crosses: 20},
            {name: "Wilson Blade 98 (16x19)", mass: 321,SW: 325, RA: 62, Hz: 130, TW: 14.2, headsize: 98,  mains: 16, crosses: 19},
            {name: "Babolat Pure Aero",  mass: 318, SW: 324, RA: 67, Hz: 145, TW: 14.0, headsize: 100, mains: 16, crosses: 19},
            {name: "Head Speed Pro",  mass: 326, SW: 331, RA: 60, Hz: 133, TW: 14.3, headsize: 100, mains: 18, crosses: 20},
            {name: "Yonex EZONE 98",  mass: 322, SW: 318, RA: 65, Hz: 140, TW: 13.9, headsize: 98, mains: 16, crosses: 19},
            {name: "Yonex VCORE 95",  mass: 326, SW: 322, RA: 63, Hz: 138, TW: 13.5, headsize: 95, mains: 16, crosses: 20}
        ];

        // SUB-EQUATIONS
        const DASI = (r) => (r.RA * r.Hz) / r.mass;
        const TSC = (r) => (Math.pow(r.TW, 2)) / r.headsize;
        const SLDM = (r) => (r.headsize * 100) / (r.mains * r.crosses);

        // SETTING TARGETS
        let ideal_SW = 320;
        if (style === "Aggressive Baseliner") ideal_SW += 5;
        if (bh === "One-Handed") ideal_SW -= 3;
        if (wingspan_cm > height_cm) ideal_SW += 3; // Positive ape index

        let ideal_SLDM = 31.0;
        if (grip === "Semi-Western" || grip === "Western") ideal_SLDM = 32.5; // Needs open stringbed
        
        let max_safe_mass = (weight_kg * 4.8) * gender_scalar;

        let results = [];

        rackets.forEach(r => {
            let biomech_fit = Math.abs(r.SW - ideal_SW) * 0.8 + Math.abs(TSC(r) - 2.05) * 5;
            let tactical_loss = Math.abs(SLDM(r) - ideal_SLDM) * 2.5;
            
            let mass_overage = Math.max(0, r.mass - max_safe_mass);
            let fatigue = mass_overage > 0 ? (Math.exp(mass_overage * 0.5) - 1) : 0;
            
            let shock = DASI(r) * injury_history;
            
            let total_cost = biomech_fit + tactical_loss + fatigue + shock;
            
            // Convert cost to a % match score (approximate logic)
            // A cost of 0 is 100%. A cost of 20+ is bad.
            let match_score = Math.max(0, 100 - (total_cost * 1.5));
            
            results.push({
                name: r.name,
                cost: total_cost,
                score: match_score.toFixed(1) + "%",
                specs: {
                    weight: r.mass + "g",
                    sw: r.SW,
                    ra: r.RA,
                    dynamic: r.Hz
                }
            });
        });

        // Sort by lowest cost
        results.sort((a, b) => a.cost - b.cost);

        return new Response(JSON.stringify({
            success: true,
            best_match: results[0],
            all_results: results.slice(0, 3)
        }), {
            headers: { "Content-Type": "application/json" }
        });
        
    } catch (error) {
        return new Response(JSON.stringify({ success: false, error: error.toString() }), {
            status: 500,
            headers: { "Content-Type": "application/json" }
        });
    }
}
