class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        l = 0
        r = len(s) - 1
        while l < r :
            if s[l].lower() in "aeiou" and s[r].lower() in 'aeiou':
                x = s[l]
                s[l] = s[r]
                s[r] = x   
                l += 1
                r -= 1             
            elif s[l].lower() in "aeiou" and s[r].lower() not in 'aeiou':
                r -= 1
            elif s[l].lower()  not in "aeiou" and s[r].lower() in 'aeiou':
                l += 1
            elif s[l].lower() not in "aeiou" and s[r].lower() not in 'aeiou':
                l += 1
                r -= 1
        return ''.join(s)