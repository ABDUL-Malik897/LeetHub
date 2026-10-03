from collections import deque


class Solution(object):

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        queue = deque()
        fresh = 0

        # Find all rotten and fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0

        # Multi-source BFS
        while queue and fresh > 0:
            size = len(queue)

            for _ in range(size):
                i, j = queue.popleft()

                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        queue.append((ni, nj))

            minutes += 1

        if fresh > 0:
            return -1

        return minutes