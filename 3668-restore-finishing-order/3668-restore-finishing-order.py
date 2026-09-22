class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in order:
            if i in friends:
                ans.append(i)
            else:
                continue
        return ans
        