class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for i, ch in enumerate(s):
            rev = 27 - (ord(ch) - ord('a') + 1)
            res = rev * (i + 1)
            n = n + res
        return n