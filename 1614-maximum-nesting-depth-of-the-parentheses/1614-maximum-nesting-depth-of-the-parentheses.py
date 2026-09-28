class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = 0
        m = 0
        for i in s:
            if i == "(":
                d += 1
                m = max(m,d)
            elif i == ")":
                d -= 1
        return m