class Solution(object):
    def beautifulSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {0: 1}
        xor = 0
        count = 0

        for num in nums:
            xor ^= num

            if xor in freq:
                count += freq[xor]

            freq[xor] = freq.get(xor, 0) + 1

        return count