class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = []
        n = len(nums)
        for i in range(n):
            if n % (i + 1) == 0:
                x.append(nums[i])
        return sum([(j*j) for j in x])
