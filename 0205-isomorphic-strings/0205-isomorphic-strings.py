class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return false
        map1={}
        map2={}

        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]

            if char1 in map1:
                if map1[char1] != char2:
                    return False
            
            if char2 in map2:
                if map2[char2] != char1:
                    return False
            map1[char1] = char2
            map2[char2] = char1
        return True