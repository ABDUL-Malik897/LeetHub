class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = nums[::-1]
        ans = nums + n
        return ans
        
        