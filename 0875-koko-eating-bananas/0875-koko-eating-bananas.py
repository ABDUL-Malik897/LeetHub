class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = max(1, (sum(piles) + h - 1) // h)
        r = max(piles)
        ans = r
        while l <= r:
            m = (l + r) // 2
            total = 0
            for pile in piles:
                total += (pile + m- 1) // m
            if total <= h:
                ans = m 
                r = m - 1
            else:
                l = m + 1
        return ans