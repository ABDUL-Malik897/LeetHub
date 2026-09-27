class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        ans = ""

        for word in words:
            total = sum(weights[ord(c) - ord('a')] for c in word)
            ans += chr(ord('z') - total % 26)

        return ans