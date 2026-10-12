class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sets = set()
        left = 0
        maxLength = 0
        for right in range(len(s)):
            while s[right] in sets:
                    sets.remove(s[left])
                    left += 1
            sets.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        

        return maxLength
    