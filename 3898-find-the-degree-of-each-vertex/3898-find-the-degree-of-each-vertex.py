class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        n = len(matrix[0])
        for i in range(n):
            count = 0
            for j in range(n):
                if matrix[i][j] == 1:
                    count += 1 
            ans.append(count)
        return ans