class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        ans = ''
        for i in words:
            total = 0
            for j in i:
                index = ord(j) - ord('a')
                total += weights[index]
            r = total % 26
            index = 25 - r
            char = chr(ord('a') + index)
            ans = ans + char
        return ans

                
