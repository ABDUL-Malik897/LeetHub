/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    let left = 0
    let right = nums.length - 1
    function build(l, r) {
        if (l > r) return null
        let mid = Math.floor((l + r)/ 2) 
        let root = new TreeNode(nums[mid])
        root.left = build(l,mid - 1)
        root.right = build(mid + 1, r)
        return root
    }
    return build(left ,right)
};