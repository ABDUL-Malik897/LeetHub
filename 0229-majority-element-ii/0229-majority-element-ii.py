class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = {}
        result = []
        limit = len(nums) // 3

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num, count in counts.items():
            if count > limit:
                result.append(num)

        return result