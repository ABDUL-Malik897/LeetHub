class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in words:
            ok = True
            for j in i :
                if j not in allowed:
                    ok = False
                    break
            if ok:
                count += 1
        return count
        