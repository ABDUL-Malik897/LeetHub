class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        count = 0
        s = str(digit)
        for i in nums:
            srt = str(i)
            if s in srt:
                count += srt.count(s)
        return count
        