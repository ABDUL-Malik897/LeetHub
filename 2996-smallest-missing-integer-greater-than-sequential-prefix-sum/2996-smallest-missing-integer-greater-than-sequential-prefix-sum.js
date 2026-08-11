/**
 * @param {number[]} nums
 * @return {number}
 */
var missingInteger = function(nums) {
    let sum = nums[0]
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] + 1 === nums[i + 1]) {
            sum += nums[i+1]
        } else {
            break
        }
    }  
    let x = sum
    while (nums.includes(x)) {
        x++
    }  
    return x
};