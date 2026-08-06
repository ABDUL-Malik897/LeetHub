/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
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
        return same(x.left , y.right) && same(x.right, y.left)
    }
    if (!root) return true;
    p = root.left
    q = root.right
    let isSame = same(p,q)
    return isSame
};