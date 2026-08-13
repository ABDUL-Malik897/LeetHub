/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function(n, k) {
    let nums = [];
    for (let i = 1; i <= n; i++) {
        nums.push(i);
    }
    let factorial = 1;
    for (let i = 1; i < n; i++) {
        factorial *= i;
    }
    k--; 
    let result = "";
    for (let i = n; i > 0; i--) {
        let index = Math.floor(k / factorial);
        result += nums[index];
        nums.splice(index, 1);
        k %= factorial;
        if (i > 1) {
            factorial = factorial / (i - 1);
        }
    }
    return result;
};