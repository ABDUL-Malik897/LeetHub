class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        r1 =  version1.split('.')
        r2 =  version2.split('.')
        n = max(len(r1), len(r2))

        for i in range(n):
            a = int(r1[i]) if i < len(r1) else 0
            b = int(r2[i]) if i < len(r2) else 0

            if a < b:
                return -1
            elif a > b:
                return 1

        return 0
