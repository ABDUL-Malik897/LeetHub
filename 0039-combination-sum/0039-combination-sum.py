class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                # Same index: reuse the candidate
                backtrack(i, remaining - candidates[i])

                path.pop()

        backtrack(0, target)
        return res