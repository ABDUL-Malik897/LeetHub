class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        seenA = set()
        seenB = set()
        ans = []
        count = 0
        n = len(B)
        for i in range(n):
            seenA.add(A[i])
            seenB.add(B[i])
            if A[i] == B[i]:
                count += 1
            else:
                if B[i] in seenA:
                    count += 1
                if A[i] in seenB:
                    count += 1
            ans.append(count)
        return ans
            
