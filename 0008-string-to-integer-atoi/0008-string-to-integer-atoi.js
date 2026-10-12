/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    let i = 0;
    let n = s.length;

    while (i < n && s[i] === ' ') {
        i++;
    }

    let sign = 1;
    if (i < n && (s[i] === '+' || s[i] === '-')) {
        sign = s[i] === '-' ? -1 : 1;
        i++;
    }

    let result = 0;

    while (i < n && s[i] >= '0' && s[i] <= '9') {
        result = result * 10 + (s[i] - '0');
        i++;
    }

    result *= sign;

    const INT_MAX = 2147483647;
    const INT_MIN = -2147483648;

    if (result > INT_MAX) return INT_MAX;
    if (result < INT_MIN) return INT_MIN;

    return result;
};