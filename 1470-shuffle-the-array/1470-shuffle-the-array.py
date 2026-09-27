class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = nums[:n]
        y = nums[n:]
        z = []
        i = 0
        while i < n:
            z.append(x[i])
            z.append(y[i])
            i += 1
        return z