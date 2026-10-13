class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m = {}
        for n in arr:
            m[n] = m.get(n,0) + 1
        ans = -1

        for x,y in m.items():
            if x == y:
                ans = max(ans,x)
        return ans