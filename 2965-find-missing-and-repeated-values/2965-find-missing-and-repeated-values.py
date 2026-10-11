class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        N = n * n

        actual_sum = 0
        actual_sq_sum = 0

        for row in grid:
            for x in row:
                actual_sum += x
                actual_sq_sum += x * x

        expected_sum = N * (N + 1) // 2
        expected_sq_sum = N * (N + 1) * (2 * N + 1) // 6

        diff = actual_sum - expected_sum
        sq_diff = actual_sq_sum - expected_sq_sum

        total = sq_diff // diff
        repeated = (diff + total) // 2
        missing = (total - diff) // 2

        return [repeated, missing]