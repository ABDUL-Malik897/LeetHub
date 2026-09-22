class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less,equal,greater = [],[],[]
        for i in nums:
            if i < pivot :
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else :
                greater.append(i)
        return less + equal + greater
        