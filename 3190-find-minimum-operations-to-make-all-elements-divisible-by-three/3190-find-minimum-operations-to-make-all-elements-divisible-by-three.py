class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        op = 0
        for i in nums:
            if i % 3 != 0:
                op += 1
        return op
                