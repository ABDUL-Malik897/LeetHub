/**
 * @param {number[]} piles
 * @return {number}
 */
var stoneGameII = function(piles) {
    let n = piles.length;
    let suffix = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; i--) {
        suffix[i] = suffix[i + 1] + piles[i];
    }
    let memo = new Map();
    function solve(i, M) {
        if (i >= n) return 0;
        let key = i + "," + M;
        if (memo.has(key)) {
            return memo.get(key);
        }
        let best = 0;
        for (let X = 1; X <= 2 * M && i + X <= n; X++) {
            let opponent = solve(i + X, Math.max(M, X));
            let current = suffix[i] - opponent;
            best = Math.max(best, current);
        }
        memo.set(key, best);
        return best;
    }
    return solve(0, 1);
};