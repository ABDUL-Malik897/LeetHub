# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def makeTree(l,r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left = makeTree(l, mid - 1)
            node.right = makeTree(mid + 1, r)
            return node
        return makeTree(0,len(nums) - 1)
        


