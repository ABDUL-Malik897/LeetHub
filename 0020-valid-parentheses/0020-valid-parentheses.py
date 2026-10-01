class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                n.append(i)
            else :
                if not n:
                    return False
                if i == ")" and n[-1] != "(":
                    return False
                if i == "}" and n[-1] != "{":
                    return False
                if i == "]" and n[-1] != "[":
                    return False 
                n.pop(-1)  
        return not n
        