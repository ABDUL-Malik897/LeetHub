class Solution(object):

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        maximum = 0

        for i in range(rows):

            # Build histogram for current row
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Find largest rectangle in histogram
            stack = [-1]

            for j in range(cols):
                while stack[-1] != -1 and heights[stack[-1]] > heights[j]:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    maximum = max(maximum, h * w)

                stack.append(j)

            # Process remaining bars
            while stack[-1] != -1:
                h = heights[stack.pop()]
                w = cols - stack[-1] - 1
                maximum = max(maximum, h * w)

        return maximum