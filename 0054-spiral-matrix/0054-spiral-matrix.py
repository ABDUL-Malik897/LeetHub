class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        left = 0
        right = n - 1
        bottom = m - 1
        res = []
        while top <= bottom and left <= right:
            for i in range(left,right + 1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top,bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for j in range(bottom, top - 1, -1):
                    res.append(matrix[j][left])
                left += 1
        return res
            