class Solution(object):
    def minInsertions(self, s):
        ans = 0
        need = 0

        for i in s:
            if i == "(":
                if need % 2 == 1:
                    ans += 1
                    need -= 1

                need += 2

            else:
                need -= 1

                if need < 0:
                    ans += 1
                    need = 1

        return ans + need