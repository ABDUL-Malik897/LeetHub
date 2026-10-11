class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = ''
        for i in s:
            if i not in h:
                h = h + i
        return len(h)
