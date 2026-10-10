class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for i in range(1,k + 1):
            idx = nums.index(min(nums))
            nums[idx] = min(nums) * multiplier
        return nums