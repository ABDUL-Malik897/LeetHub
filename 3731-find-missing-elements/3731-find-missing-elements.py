class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        minN = min(nums)
        maxN = max(nums)
        ans = []
        while minN != maxN:
            if minN not in nums:
                ans.append(minN)
            minN += 1
        return ans
        
        