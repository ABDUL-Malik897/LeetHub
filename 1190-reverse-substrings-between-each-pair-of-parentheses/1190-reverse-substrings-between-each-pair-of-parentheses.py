class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        st = []

        for ch in s:

            if ch == '(':
                st.append(ch)

            elif ch == ')':
                temp = []

                # Take characters out until '('
                while st[-1] != '(':
                    temp.append(st.pop())

                # Remove '('
                st.pop()

                # Put reversed characters back
                st.extend(temp)

            else:
                st.append(ch)

        return ''.join(st)