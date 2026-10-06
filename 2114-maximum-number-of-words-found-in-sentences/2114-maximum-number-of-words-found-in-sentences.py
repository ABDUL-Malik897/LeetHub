class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxi = 0
        for i in sentences:
            words = i.split()
            maxi = max(maxi,len(words))
        return maxi