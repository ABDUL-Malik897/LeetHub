class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Count frequency of each number
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Bucket: index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # Take elements from highest frequency to lowest
        ans = []

        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                ans.append(num)

                if len(ans) == k:
                    return ans

        return ans