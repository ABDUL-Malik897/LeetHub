class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)
        ans = 0
        while i < n - 1:
            ans += abs(ord(s[i])- ord(s[i+1]))
            i += 1
        return ans