class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        maxLocal = []
        for i in range(len(grid) - 2):
            row = []
            for j in range(len(grid) - 2):
                maximum = 0
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        maximum = max(maximum, grid[r][c])
                row.append(maximum)
            maxLocal.append(row)
        return maxLocal