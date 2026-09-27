class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        
        for i in nums:
            count = 0
            a = str(i)
            for j in a:
                count += int(j)
            ans.append(count) 
        return min(ans)