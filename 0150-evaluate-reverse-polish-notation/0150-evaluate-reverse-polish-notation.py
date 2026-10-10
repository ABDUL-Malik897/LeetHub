class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                s.append(int(tokens[i]))
            else:
                b = s.pop()
                a = s.pop()
                if tokens[i] == "+":
                    s.append(a + b)
                elif tokens[i] == "-":
                    s.append(a - b)
                elif tokens[i] == "*":
                    s.append(a * b)
                elif tokens[i] == "/":
                    result = abs(a) // abs(b)
                    if (a < 0) != (b < 0):
                        result = -result
                    s.append(result)
        return s[0]
