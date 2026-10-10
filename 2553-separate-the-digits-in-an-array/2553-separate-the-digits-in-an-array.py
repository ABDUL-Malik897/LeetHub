class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = "".join(str(x) for x in nums)
        return [int(x) for x in s]