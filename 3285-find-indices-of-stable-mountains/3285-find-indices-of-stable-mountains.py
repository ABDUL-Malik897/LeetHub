class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        count = []
        for i in range(1,len(height)):
            if height[i - 1] > threshold:
                count.append(i)
        return count
