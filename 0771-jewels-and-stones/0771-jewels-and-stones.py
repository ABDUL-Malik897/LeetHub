class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        j = set(jewels)
        count = 0
        for i in j:
            for x in stones:
                if i in x:
                    count += 1
        return count