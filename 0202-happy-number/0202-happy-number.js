/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    // const digits = 
    const seen = new Set()
    while (n !== 1) {
        if (seen.has(n)) {
            return false
        }
        seen.add(n);
        n = Array.from(String(n), Number).reduce((sum, digit) => sum + digit ** 2, 0)
    }
    return true
};