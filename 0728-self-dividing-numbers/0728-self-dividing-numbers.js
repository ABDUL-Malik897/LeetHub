/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    let result =[]
    for (let num = left; num <= right; num++) {
        let isValid = true
        for (let digit of String(num)) {
            let d = Number(digit)
            if (d === 0 || num % d !=0) {
                isValid = false
                break
            }            
        }
        if(isValid) {
            result.push(num)
        }
    }
    return result
};