class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        answer = []
        for i in range(0,len(boxes)):
            operations = 0
            for j in range(0,len(boxes)):
                if boxes[j] == '1':
                    operations += abs(i - j)
            answer.append(operations)
        return answer