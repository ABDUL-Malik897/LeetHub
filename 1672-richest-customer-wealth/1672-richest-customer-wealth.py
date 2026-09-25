class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        digit_sums = [sum(int(digit) for digit in num) for num in accounts]
        return max(digit_sums)