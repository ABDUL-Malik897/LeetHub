class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        seen = set(nums)
        for i in range(1,len(nums)+1):
            if i not in seen:
                arr.append(i)
        return arr