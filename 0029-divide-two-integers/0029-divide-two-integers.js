/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    let count = 0
    let d1 = divisor
    let d2 = dividend
    
    if (divisor < 0) {
        d1 = Math.abs(divisor)
    }
    if (dividend < 0) {
        d2 = Math.abs(dividend)
    }
    while (d2 >= d1) {
        let temp = d1
        let mul = 1
        while (d2 >= temp + temp) {
            temp += temp
            mul += mul
        }
        d2 -= temp
        count += mul
    }
    if (dividend === -2147483648 && divisor === -1) {
        return 2147483647;
    }
    const negative = (dividend < 0) !== (divisor < 0)
    if (negative) {
        count = -count
    }

    return count

};