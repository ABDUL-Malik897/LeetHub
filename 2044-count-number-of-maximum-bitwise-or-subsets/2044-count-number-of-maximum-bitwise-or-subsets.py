class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = 0
        for x in nums:
            target |= x

        def dfs(i, cur):
            if i == len(nums):
                return 1 if cur == target else 0

            return dfs(i + 1, cur | nums[i]) + dfs(i + 1, cur)

        return dfs(0, 0)