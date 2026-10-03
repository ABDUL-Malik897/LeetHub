import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        j = int(math.sqrt(c))
        while i <= j: 
            if (i ** 2) + (j ** 2) == c:
                return True
            elif (i ** 2) + (j ** 2) < c:
                i += 1
            elif (i ** 2) + (j ** 2) > c:
                j -= 1

        return False
