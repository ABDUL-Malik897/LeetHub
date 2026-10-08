class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        i = 0
        j = len(nums) - 1
        pos = len(nums) - 1
        while i <= j:
            if nums[i] ** 2 < nums[j] ** 2:
                result[pos] = nums[j] ** 2
                j -= 1
            else:
                result[pos] = nums[i] ** 2
                i += 1
            pos -= 1
        return result
            

