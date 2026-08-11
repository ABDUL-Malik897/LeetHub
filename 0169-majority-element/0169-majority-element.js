/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let candidate 
    let count = 0
    for (let i of nums) {
        if (count === 0) {
            candidate = i
        }
        if (i === candidate) {
            count ++
        } else {
            count --
        }
    }
    return candidate
};