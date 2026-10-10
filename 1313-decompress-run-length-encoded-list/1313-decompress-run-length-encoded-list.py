class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            val = nums[i + 1]
            n += [val] * freq
        return n
