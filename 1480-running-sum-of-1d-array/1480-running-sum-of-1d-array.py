class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        total = 0

        for number in nums:
            total = total + number
            ans.append(total)
        return ans