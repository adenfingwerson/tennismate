export async function onRequestPost(context) {
    try {
        const p = await context.request.json();

        const height_in = parseFloat(p.height) || 72; 
        const weight_lbs = parseFloat(p.weight) || 160; 
        const wingspan_in = parseFloat(p.wingspan) || 72;
        const grip = p.grip || "Semi-Western";
        const style = p.style || "All-Court Player";
        const bh = p.bh || "Two-Handed";

        const height_cm = height_in * 2.54;
        const wingspan_cm = wingspan_in * 2.54;
        const weight_kg = weight_lbs * 0.453592;
        const gender_scalar = 1.0; 
        const injury_history = 0.25; 

        const rackets = [
            // BABOLAT
            {name: "Babolat Pure Drive (2021)", mass: 318, SW: 320, RA: 71, Hz: 155, TW: 14.5, headsize: 100, mains: 16, crosses: 19, osint_plushness: 0},
            {name: "Babolat Pure Aero (2023)", mass: 318, SW: 322, RA: 65, Hz: 145, TW: 14.0, headsize: 100, mains: 16, crosses: 19, osint_plushness: 2},
            {name: "Babolat Pure Aero 98", mass: 323, SW: 327, RA: 65, Hz: 148, TW: 14.2, headsize: 98, mains: 16, crosses: 20, osint_plushness: 1},
            {name: "Babolat Pure Strike 16x19 (Gen 4)", mass: 323, SW: 330, RA: 68, Hz: 150, TW: 14.8, headsize: 98, mains: 16, crosses: 19, osint_plushness: 3},
            {name: "Babolat Pure Strike 18x20 (Gen 4)", mass: 323, SW: 332, RA: 68, Hz: 150, TW: 15.0, headsize: 98, mains: 18, crosses: 20, osint_plushness: 3},
            {name: "Babolat Pure Strike 97", mass: 329, SW: 325, RA: 65, Hz: 142, TW: 13.9, headsize: 97, mains: 16, crosses: 20, osint_plushness: 2},
            
            // WILSON
            {name: "Wilson Pro Staff 97 v14", mass: 330, SW: 320, RA: 66, Hz: 135, TW: 13.8, headsize: 97, mains: 16, crosses: 19, osint_plushness: 2},
            {name: "Wilson Blade 98 16x19 v9", mass: 321, SW: 325, RA: 62, Hz: 130, TW: 14.2, headsize: 98, mains: 16, crosses: 19, osint_plushness: 1},
            {name: "Wilson Blade 98 18x20 v9", mass: 321, SW: 327, RA: 62, Hz: 130, TW: 14.4, headsize: 98, mains: 18, crosses: 20, osint_plushness: 1},
            {name: "Wilson Clash 100 v2", mass: 312, SW: 313, RA: 57, Hz: 110, TW: 13.5, headsize: 100, mains: 16, crosses: 19, osint_plushness: 8},
            {name: "Wilson Clash 98 v2", mass: 326, SW: 325, RA: 60, Hz: 115, TW: 14.0, headsize: 98, mains: 16, crosses: 20, osint_plushness: 6},
            {name: "Wilson Shift 99 Pro v1", mass: 332, SW: 330, RA: 68, Hz: 140, TW: 14.5, headsize: 99, mains: 18, crosses: 20, osint_plushness: 4},
            {name: "Wilson Ultra 100 v4", mass: 318, SW: 317, RA: 70, Hz: 148, TW: 14.2, headsize: 100, mains: 16, crosses: 19, osint_plushness: 2},

            // HEAD
            {name: "Head Speed Pro 2024", mass: 326, SW: 331, RA: 60, Hz: 133, TW: 14.3, headsize: 100, mains: 18, crosses: 20, osint_plushness: 3},
            {name: "Head Speed MP 2024", mass: 318, SW: 325, RA: 60, Hz: 133, TW: 14.1, headsize: 100, mains: 16, crosses: 19, osint_plushness: 3},
            {name: "Head Radical MP 2023", mass: 318, SW: 323, RA: 65, Hz: 142, TW: 14.0, headsize: 98, mains: 16, crosses: 19, osint_plushness: 2},
            {name: "Head Radical Pro 2023", mass: 332, SW: 330, RA: 64, Hz: 140, TW: 14.5, headsize: 98, mains: 16, crosses: 19, osint_plushness: 2},
            {name: "Head Gravity Pro 2023", mass: 332, SW: 333, RA: 59, Hz: 125, TW: 15.0, headsize: 100, mains: 18, crosses: 20, osint_plushness: 1},
            {name: "Head Gravity Tour 2025", mass: 323, SW: 325, RA: 61, Hz: 128, TW: 14.6, headsize: 98, mains: 16, crosses: 19, osint_plushness: 2},
            {name: "Head Extreme MP 2024", mass: 318, SW: 322, RA: 63, Hz: 138, TW: 14.0, headsize: 100, mains: 16, crosses: 19, osint_plushness: 2},
            {name: "Head Extreme Pro 2024", mass: 332, SW: 331, RA: 63, Hz: 138, TW: 14.4, headsize: 98, mains: 16, crosses: 19, osint_plushness: 2},
            {name: "Head Prestige Pro 2023", mass: 337, SW: 330, RA: 60, Hz: 130, TW: 14.2, headsize: 98, mains: 18, crosses: 20, osint_plushness: 1},
            {name: "Head Boom Pro 2024", mass: 326, SW: 325, RA: 64, Hz: 140, TW: 14.2, headsize: 98, mains: 16, crosses: 19, osint_plushness: 2},

            // YONEX
            {name: "Yonex EZONE 98 (2022)", mass: 323, SW: 318, RA: 65, Hz: 140, TW: 13.9, headsize: 98, mains: 16, crosses: 19, osint_plushness: 2},
            {name: "Yonex EZONE 100 (2022)", mass: 318, SW: 317, RA: 67, Hz: 144, TW: 14.3, headsize: 100, mains: 16, crosses: 19, osint_plushness: 2},
            {name: "Yonex VCORE 95 (2023)", mass: 326, SW: 322, RA: 61, Hz: 135, TW: 13.5, headsize: 95, mains: 16, crosses: 20, osint_plushness: 1},
            {name: "Yonex VCORE 98 (2023)", mass: 323, SW: 325, RA: 62, Hz: 138, TW: 14.0, headsize: 98, mains: 16, crosses: 19, osint_plushness: 1},
            {name: "Yonex VCORE 100 (2023)", mass: 318, SW: 322, RA: 65, Hz: 142, TW: 14.5, headsize: 100, mains: 16, crosses: 19, osint_plushness: 1},
            {name: "Yonex Percept 97", mass: 326, SW: 320, RA: 60, Hz: 130, TW: 13.8, headsize: 97, mains: 16, crosses: 19, osint_plushness: 1},
            {name: "Yonex Percept 97D", mass: 337, SW: 332, RA: 61, Hz: 132, TW: 14.0, headsize: 97, mains: 18, crosses: 20, osint_plushness: 1},
            {name: "Yonex Percept 100", mass: 318, SW: 318, RA: 62, Hz: 132, TW: 14.1, headsize: 100, mains: 16, crosses: 19, osint_plushness: 1},

            // TECNIFIBRE
            {name: "Tecnifibre TFight 305 ISO", mass: 323, SW: 333, RA: 64, Hz: 140, TW: 14.5, headsize: 98, mains: 18, crosses: 19, osint_plushness: 1},
            {name: "Tecnifibre TF40 305 (16x19)", mass: 323, SW: 325, RA: 64, Hz: 138, TW: 14.2, headsize: 98, mains: 16, crosses: 19, osint_plushness: 2},
            {name: "Tecnifibre TF40 305 (18x20)", mass: 323, SW: 326, RA: 64, Hz: 138, TW: 14.3, headsize: 98, mains: 18, crosses: 20, osint_plushness: 2},

            // DUNLOP
            {name: "Dunlop CX 200", mass: 323, SW: 318, RA: 64, Hz: 135, TW: 13.8, headsize: 98, mains: 16, crosses: 19, osint_plushness: 2},
            {name: "Dunlop SX 300", mass: 318, SW: 322, RA: 68, Hz: 145, TW: 14.0, headsize: 100, mains: 16, crosses: 19, osint_plushness: 1},
            {name: "Dunlop FX 500", mass: 318, SW: 320, RA: 71, Hz: 152, TW: 14.2, headsize: 100, mains: 16, crosses: 19, osint_plushness: 0}
        ];

        const DASI = (r) => {
            let effective_RA = Math.max(50, r.RA - r.osint_plushness);
            return (effective_RA * r.Hz) / r.mass;
        };
        const TSC = (r) => (Math.pow(r.TW, 2)) / r.headsize;
        const SLDM = (r) => (r.headsize * 100) / (r.mains * r.crosses);

        let ideal_SW = 320;
        if (style === "Aggressive Baseliner") ideal_SW += 5;
        if (style === "Counter-Puncher") ideal_SW -= 2;
        if (style === "Serve & Volley") ideal_SW -= 4; 
        if (bh === "One-Handed") ideal_SW -= 4; 
        
        let ape_index = wingspan_cm - height_cm;
        if (ape_index > 0) ideal_SW += (ape_index * 0.5); 

        let ideal_SLDM = 31.0;
        if (grip === "Semi-Western" || grip === "Western") ideal_SLDM = 32.5; 
        if (grip === "Eastern" || grip === "Continental") ideal_SLDM = 28.5; 
        
        let max_safe_mass = (weight_kg * 4.8) * gender_scalar;

        // NEW: TennisWarehouse-Style Algorithm Mapping
        const calcTWMetrics = (r, idealSW) => {
            let sldm = SLDM(r);
            let dasi = DASI(r);
            
            let power = 48 + (r.RA - 60) * 1.5 + (r.SW - 300) * 0.8 + (sldm - 28) * 2.5;
            power = Math.max(0, Math.min(100, power));
            
            let control = 100 - (power * 0.3) + (r.TW - 13) * 6 - (sldm - 32) * 3;
            control = Math.max(0, Math.min(100, control));
            
            let maneuverability = 96 - (r.SW - idealSW) * 1.0 - (r.mass - 300) * 0.15;
            maneuverability = Math.max(0, Math.min(100, maneuverability));
            
            let stability = 65 + (r.TW - 13) * 10 + (r.mass - 300) * 0.2;
            stability = Math.max(0, Math.min(100, stability));
            
            let comfort = 110 - (dasi * 1.0) + (r.osint_plushness * 2.5);
            comfort = Math.max(0, Math.min(100, comfort));
            
            let touch = 90 - (r.Hz - 130) * 0.8 + (r.osint_plushness * 2.0);
            touch = Math.max(0, Math.min(100, touch));
            
            let topspin = 62 + (sldm - 28) * 5 + (maneuverability * 0.05);
            topspin = Math.max(0, Math.min(100, topspin));
            
            let slice = 55 + stability * 0.3 + (r.mass - 300) * 0.15 - (sldm - 32) * 1.5;
            slice = Math.max(0, Math.min(100, slice));
            
            let groundstrokes = (power * 0.2 + control * 0.3 + topspin * 0.2 + stability * 0.3);
            let volleys = (maneuverability * 0.3 + stability * 0.3 + touch * 0.2 + control * 0.2);
            let serves = (power * 0.4 + maneuverability * 0.3 + topspin * 0.3);
            let returns = (stability * 0.4 + maneuverability * 0.3 + control * 0.3);
            
            let overall = (groundstrokes + volleys + serves + returns + power + control + maneuverability + stability + comfort + touch + topspin + slice) / 12;

            return {
                overall: parseFloat(overall.toFixed(1)),
                groundstrokes: parseFloat(groundstrokes.toFixed(1)),
                volleys: parseFloat(volleys.toFixed(1)),
                serves: parseFloat(serves.toFixed(1)),
                returns: parseFloat(returns.toFixed(1)),
                power: parseFloat(power.toFixed(1)),
                control: parseFloat(control.toFixed(1)),
                maneuverability: parseFloat(maneuverability.toFixed(1)),
                stability: parseFloat(stability.toFixed(1)),
                comfort: parseFloat(comfort.toFixed(1)),
                touch: parseFloat(touch.toFixed(1)),
                topspin: parseFloat(topspin.toFixed(1)),
                slice: parseFloat(slice.toFixed(1))
            };
        };

        let results = [];

        rackets.forEach(r => {
            let biomech_cost = Math.abs(r.SW - ideal_SW) * 0.85 + Math.abs(TSC(r) - 2.05) * 6;
            let tactical_cost = Math.abs(SLDM(r) - ideal_SLDM) * 3.0;
            let mass_overage = Math.max(0, r.mass - max_safe_mass);
            let fatigue_cost = mass_overage > 0 ? (Math.exp(mass_overage * 0.6) - 1) : 0;
            let shock_cost = DASI(r) * injury_history;
            let safety_cost = fatigue_cost + shock_cost;
            let total_cost = biomech_cost + tactical_cost + safety_cost;
            
            let match_score = Math.max(0, Math.min(99.9, 100 - (total_cost * 1.2)));
            let bio_score = Math.max(0, Math.min(100, 100 - (biomech_cost * 2.5)));
            let tac_score = Math.max(0, Math.min(100, 100 - (tactical_cost * 2.5)));
            let safe_score = Math.max(0, Math.min(100, 100 - (safety_cost * 2.5)));
            
            let tw_ratings = calcTWMetrics(r, ideal_SW);

            results.push({
                name: r.name,
                cost: total_cost,
                score: match_score,
                bio_score: bio_score,
                tac_score: tac_score,
                safe_score: safe_score,
                tw_ratings: tw_ratings,
                specs: {
                    weight: r.mass,
                    sw: r.SW,
                    ra: r.RA,
                    dynamic: r.Hz,
                    pattern: r.mains + "x" + r.crosses
                }
            });
        });

        results.sort((a, b) => a.cost - b.cost);

        return new Response(JSON.stringify({
            success: true,
            best_match: results[0],
            runner_up_1: results[1],
            runner_up_2: results[2]
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
