class Solution(object):

    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        remove = set()

        # Find invalid ')'
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)

            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)

        # Any '(' left in stack is invalid
        for i in stack:
            remove.add(i)

        # Build the answer without invalid parentheses
        ans = []

        for i, ch in enumerate(s):
            if i not in remove:
                ans.append(ch)

        return ''.join(ans)