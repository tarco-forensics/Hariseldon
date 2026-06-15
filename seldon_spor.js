/*
T2SAIM SPOR SELDON — James Monte Carlo Motoru
NTZ-49 BTTFR uyarlamasi: 1000 agent × 100K iterasyon
*/
function jamesSeldonSim(evGucu, depGucu, evForm, depForm, iterasyon = 10000) {
    // Skor dagilimi: Poisson(λ) 
    // λ_ev = evGucu * evForm * 1.2 (ev avantaji)
    // λ_dep = depGucu * depForm * 0.9
    let evWin = 0, draw = 0, depWin = 0, golToplam = 0;
    const evLambda = evGucu * evForm * 1.25;
    const depLambda = depGucu * depForm * 0.85;
    
    for (let i = 0; i < iterasyon; i++) {
        const evGol = poissonSample(evLambda);
        const depGol = poissonSample(depLambda);
        golToplam += evGol + depGol;
        if (evGol > depGol) evWin++;
        else if (evGol === depGol) draw++;
        else depWin++;
    }
    
    return {
        ev: evWin / iterasyon,
        beraberlik: draw / iterasyon,
        dep: depWin / iterasyon,
        golOrt: golToplam / iterasyon,
        evYenilmez: (evWin + draw) / iterasyon
    };
}

function poissonSample(lambda) {
    // Knuth'un algoritması
    const L = Math.exp(-lambda);
    let k = 0, p = 1;
    while (p > L) {
        k++;
        p *= Math.random();
    }
    return k - 1;
}

function selDonBahis(takimAd, rakAd, guc, form, rakipGuc, rakipForm, oran) {
    const sim = jamesSeldonSim(guc, rakipGuc, form, rakipForm, 25000);
    const edge = (sim.evYenilmez * oran) - 1;
    return {
        takim: takimAd, rakip: rakAd,
        evYenilmez: +(sim.evYenilmez * 100).toFixed(1),
        golOrt: +sim.golOrt.toFixed(2),
        edge: +(edge * 100).toFixed(1),
        gir: edge > 0
    };
}
