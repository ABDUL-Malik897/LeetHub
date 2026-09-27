class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if i % 2 != 0:
                count -= nums[i]
            else:
                count += nums[i] 
        return count