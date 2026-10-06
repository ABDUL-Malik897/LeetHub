class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        for i in s:
            if st and i == st[-1]:
                st.pop()
            else:
                st.append(i)

        return ''.join(st)