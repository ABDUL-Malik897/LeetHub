class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        depth = 0
        result = ""

        for ch in s:
            if ch == '(':
                depth += 1

                if depth > 1:
                    result += ch
            else:
                if depth > 1:
                    result += ch
                depth -= 1

        return result