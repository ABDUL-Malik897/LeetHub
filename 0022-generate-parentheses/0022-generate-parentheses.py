class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def backtrack(currentString, open, close) :
            if len(currentString) == n * 2 :
                result.append(currentString)
                return
            if open < n :
                backtrack(currentString + "(", open + 1, close)
            
            if close < open :
                backtrack(currentString + ")", open, close + 1)
        backtrack("", 0, 0)
        return result