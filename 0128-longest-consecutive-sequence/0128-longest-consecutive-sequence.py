class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        streak = 0
        for num in numSet:
            if (num -1) not in numSet:
                curr = num
                currStreak = 1
                while (curr + 1) in numSet:
                    curr += 1
                    currStreak += 1
                streak = max(streak, currStreak)
        return streak