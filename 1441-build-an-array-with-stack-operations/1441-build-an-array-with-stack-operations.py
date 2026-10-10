class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1,target[-1] + 1):
            ans.append("Push")
            if i not in target:
                ans.append("Pop")
        return ans