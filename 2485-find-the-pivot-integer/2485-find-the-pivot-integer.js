/**
 * @param {number} n
 * @return {number}
 */
var pivotInteger = function(n) {
    // x² = n(n+1)/2
    // total = n(n+1)/2
    // x² = total
    let sum = (n*(n+1)/2)
    let pivot = parseInt(Math.sqrt(sum))
    if (pivot * pivot === sum) return pivot 
    else return -1
};