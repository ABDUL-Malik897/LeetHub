class Solution(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        req = {end: cnt for end, cnt in requirements}
        max_inv = max(req.values())

        dp = [0] * (max_inv + 1)
        dp[0] = 1

        for length in range(1, n + 1):
            new_dp = [0] * (max_inv + 1)
            window = 0

            for inv in range(max_inv + 1):
                window += dp[inv]

                if inv - length >= 0:
                    window -= dp[inv - length]

                new_dp[inv] = window % MOD

            dp = new_dp

            end = length - 1
            if end in req:
                required = req[end]
                if required > max_inv:
                    return 0

                keep = dp[required]
                dp = [0] * (max_inv + 1)
                dp[required] = keep

        return sum(dp) % MOD