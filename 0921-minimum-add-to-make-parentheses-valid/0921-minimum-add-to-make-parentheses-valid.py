class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        top = -1
        for i in s:
            if i == "(":
                st.append(i)
                top += 1
            else:
                if top >= 0 and st[top] == "(":
                    st.pop()
                    top -= 1
                else:
                    st.append(i)
                    top += 1

        return len(st)