/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var missingMultiple = function(nums, k) {
    let multiple = k;

    while (nums.includes(multiple)) {
        multiple += k;
    }

    return multiple;
};