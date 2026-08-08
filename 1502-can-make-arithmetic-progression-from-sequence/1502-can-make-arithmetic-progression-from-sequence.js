/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canMakeArithmeticProgression = function(arr) {
    let sorted = arr.sort((a,b) => a-b)
    let diff = sorted[1] - sorted[0]
    if (sorted.length >= 2) {
        for (let i = 2; i<= sorted.length-1; i++) {
            let current = sorted[i] - sorted[i-1]
            if ( diff !== current) {
                return false
            } 
        }
        return true
    }
    
};