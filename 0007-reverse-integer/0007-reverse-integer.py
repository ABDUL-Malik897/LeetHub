class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        x = abs(x)

        limit = 2147483648 if negative else 2147483647
        rev = 0

        while x > 0:
            digit = x % 10
            x //= 10

                # Check overflow before rev * 10 + digit
            if rev > limit // 10 or (rev == limit // 10 and digit > limit % 10):
                return 0
            rev = rev * 10 + digit

        return -rev if negative else rev