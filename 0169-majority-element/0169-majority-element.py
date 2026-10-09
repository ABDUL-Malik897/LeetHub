class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        c = 1
        for i in nums[1:]:
            if c == 0:
                m = i
                c = 1
            elif m != i:
                c -= 1
            else:
                c += 1
        return m