class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        def solve(index, current_xor):
            if index == n:
                return current_xor

            # Don't take nums[index]
            not_take = solve(index + 1, current_xor)

            # Take nums[index]
            take = solve(index + 1, current_xor ^ nums[index])

            return not_take + take

        return solve(0, 0)