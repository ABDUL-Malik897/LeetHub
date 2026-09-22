class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        for i in range(n):
            l = 0
            r = 0
            for j in range(0,i):
                l += nums[j]
            for j in range(i+1,n):
                r += nums[j]
            ans.append(abs(l - r))
        return ans