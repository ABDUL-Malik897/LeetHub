class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] ** 2 < nums[j] ** 2:
                result = [nums[j] ** 2] + result
                j -= 1
            else:
                result = [nums[i] ** 2] + result
                i += 1
        return result
            

