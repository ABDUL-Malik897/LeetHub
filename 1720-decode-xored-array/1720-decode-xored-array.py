class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first]
        for i in range(1,len(encoded) + 1):
            n = encoded[i-1] ^ arr[i-1]
            arr.append(n)
        return arr

