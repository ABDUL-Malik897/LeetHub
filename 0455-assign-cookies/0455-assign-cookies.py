class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        i = 0  # Children
        j = 0  # Cookies
        count = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1

            j += 1

        return count