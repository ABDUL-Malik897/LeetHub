class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxl = 0
        curr = 0
        i =0
        while i < len(nums):
            if nums[i] == 1:
                curr += 1
                maxl = max(maxl, curr)
            else:
                curr = 0
            i += 1
        return maxl