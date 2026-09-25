class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        ans = []
        for i in nums:
            if i in arr:
                ans.append(i)
            else :
                arr.append(i)
        return ans