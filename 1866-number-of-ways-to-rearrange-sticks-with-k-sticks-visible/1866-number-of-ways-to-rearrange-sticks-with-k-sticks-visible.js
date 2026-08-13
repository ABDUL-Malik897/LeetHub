/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var rearrangeSticks = function(n, k) {
    const MOD = 1000000007;
    let dp = Array.from(
        { length: n + 1 },
        () => new Array(k + 1).fill(0)
    );
    dp[1][1] = 1;
    for (let i = 2; i <= n; i++) {
        for (let j = 1; j <= Math.min(i, k); j++) {
            dp[i][j] =
                (dp[i - 1][j - 1] +
                (i - 1) * dp[i - 1][j]) % MOD;
        }
    }
    return dp[n][k];
};