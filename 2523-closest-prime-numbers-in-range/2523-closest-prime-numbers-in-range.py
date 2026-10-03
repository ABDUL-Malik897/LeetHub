class Solution(object):

    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        if right < 2:
            return [-1, -1]

        is_prime = [True] * (right + 1)
        is_prime[0] = False
        is_prime[1] = False

        p = 2

        while p * p <= right:
            if is_prime[p]:
                for i in range(p * p, right + 1, p):
                    is_prime[i] = False
            p += 1

        prev = -1
        best_gap = float('inf')
        ans = [-1, -1]

        for num in range(left, right + 1):
            if is_prime[num]:

                if prev != -1:
                    gap = num - prev

                    if gap < best_gap:
                        best_gap = gap
                        ans = [prev, num]

                prev = num

        return ans