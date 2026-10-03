class Solution(object):

    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)

        # XY projection: every non-zero cell contributes 1
        top = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    top += 1

        # YZ projection: maximum height in each row
        front = 0
        for i in range(n):
            front += max(grid[i])

        # ZX projection: maximum height in each column
        side = 0
        for j in range(n):
            maximum = 0
            for i in range(n):
                maximum = max(maximum, grid[i][j])
            side += maximum

        return top + front + side