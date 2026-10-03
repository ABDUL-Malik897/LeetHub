class Solution(object):

    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """

        ans = 0

        while n > 0:
            if n % 2 == 0:
                n //= 2

            else:
                if n == 1:
                    ans += 1
                    break

                if n % 4 == 1:
                    n -= 1
                else:
                    n += 1

                ans += 1

        return ans