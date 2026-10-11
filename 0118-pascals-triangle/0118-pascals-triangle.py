class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]
        for _ in range(1, numRows):
            prev = triangle[-1]
            row = [1]
            for j in range(1, len(prev)):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
            triangle.append(row)
        return triangle 