class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans = []
        for i in range(len(candies)):
            bol = (candies[i] + extraCandies) >= max(candies)
            ans.append(bol)
        return ans
