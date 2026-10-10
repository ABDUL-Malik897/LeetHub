class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        diffs = []

        for i in range(len(nums1)):
            diffs.append(abs(nums1[i] - nums2[i]))

        total = sum(diffs)

        if k >= total:
            return 0

        l = 0
        r = max(diffs)

        while l < r:
            mid = (l + r) // 2
            operations = 0

            for d in diffs:
                operations += max(0, d - mid)

            if operations > k:
                l = mid + 1
            else:
                r = mid

        target = l
        operations = 0
        answer = 0

        for d in diffs:
            operations += max(0, d - target)
            x = min(d, target)
            answer += x * x

        remaining = k - operations
        answer -= remaining * (2 * target - 1)

        return answer