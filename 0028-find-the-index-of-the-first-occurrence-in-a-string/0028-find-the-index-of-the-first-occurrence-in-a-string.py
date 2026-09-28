class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        indices = [i for i in range(len(haystack)) if haystack.startswith(needle, i)]
        if len(indices) > 0:
            return min(indices)
        else:
            return -1