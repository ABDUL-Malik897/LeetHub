/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    var same = function (x, y) {
        if (!x && !y) {
            return true
        }
        if (!x && y) {
            return false
        }
        if (x && !y) {
            return false
        }
        if (x.val !== y.val) {
            return false
        }
        return same(x.left , y.left) && same(x.right, y.right)
    }
    let isSame = same(p,q)
    return isSame
};