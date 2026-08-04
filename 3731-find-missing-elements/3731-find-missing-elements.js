/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findMissingElements = function(nums) {
    const Mymax = Math.max(...nums)
    const Mymin = Math.min(...nums)
    let MySet = new Set(nums)
    const missingArray = []
    for (let i = Mymin  ; i < Mymax ; i++) {
        if (!MySet.has(i + 1 )) {
            missingArray.push(i + 1)
        }
    }
    return missingArray
};