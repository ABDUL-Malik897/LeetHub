/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    let pivot
    for (let i = nums.length -1; i > 0; i--) {
        if (nums[i-1]<nums[i]) {
            pivot = i-1
            break
        } 
    }
    if (pivot === undefined) {
        nums = nums.reverse()
        return
    }
    for (let j = nums.length -1; j > pivot; j--) {
        if (nums[j] > nums[pivot]) {
            let temp = nums[pivot]
            nums[pivot] = nums[j]
            nums[j] = temp
            break
        }
    }
    let left = pivot + 1;
    let right = nums.length - 1;

    while (left < right) {
        let temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;

        left++;
        right--;
    }
};