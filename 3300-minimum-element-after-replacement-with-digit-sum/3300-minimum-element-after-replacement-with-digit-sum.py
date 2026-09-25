class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digit_sums = [sum(int(digit) for digit in str(num)) for num in nums]
        return min(digit_sums)