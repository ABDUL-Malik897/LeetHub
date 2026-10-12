class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(range(1, n + 1))
        result = []

        k -= 1  # Convert to zero-based indexing

        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i

        for i in range(n - 1, -1, -1):
            index = k // fact[i]
            result.append(str(nums.pop(index)))
            k %= fact[i]

        return "".join(result)