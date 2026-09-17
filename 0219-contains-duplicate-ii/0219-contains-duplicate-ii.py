class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapping = {}
        for i in range(len(nums)):
            if nums[i] in mapping:
                prev = mapping[nums[i]]
                if abs(i - prev) <= k:
                    return True
            mapping[nums[i]] = i
        return False
