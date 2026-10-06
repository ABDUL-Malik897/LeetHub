class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        p = sorted(people)
        l = 0
        r = len(p) - 1
        count = 0
        while (l <= r):
            if p[l] + p[r] <= limit:
                l += 1
            r -= 1
            count += 1
        return count


