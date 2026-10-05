class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = -1
        seen = set()
        m = -1
        for i in nums:
            if i in seen:
                d = i
            else:
                seen.add(i)
        for j in range(1,len(nums)+1):
            if j not in seen:
                m = j
                break
        return [d,m]

