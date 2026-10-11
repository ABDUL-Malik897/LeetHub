class Solution(object):
    def permute(self, nums):
        ans = []
        n = len(nums)
        def backtrack(start):
            if start == n:
                ans.append(nums[:])
                return
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack(0)
        return ans