/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    for (let i = digits.length - 1; i >= 0 ; i--) {
        if (digits[i] === 9) {
            digits[i] = 0
            
        } else {
            digits[i] = digits[i] + 1
            return digits
        }
        
    }
    if (digits.every(val => val === 0)){
            digits.unshift(1)
    }
    return digits
};