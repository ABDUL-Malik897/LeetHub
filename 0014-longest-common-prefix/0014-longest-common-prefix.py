class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        for chars in zip(*strs):
            if len(set(chars)) == 1:  
                prefix += chars[0]
            else:
                break
        return prefix
        