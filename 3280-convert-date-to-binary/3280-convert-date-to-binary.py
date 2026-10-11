class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        d = date.split("-")
        for i in range(len(d)):
            d[i] = bin(int(d[i]))[2:]
        return '-'.join(d)