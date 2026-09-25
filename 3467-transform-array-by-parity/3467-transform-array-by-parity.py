class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = nums
        for i in range(len(n)) :
            if n[i]%2 == 0:
                n[i] = 0
            else:
                n[i] = 1
        n.sort()
        return n
