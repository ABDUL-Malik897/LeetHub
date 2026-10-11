class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        v = 0
        for i in set(s):
            if i in "aeiou":
                v = max(v, s.count(i))
            else:
                c = max(c, s.count(i))

        return c + v
            