class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        r=0
        for i in range(len(columnTitle)):
            a=ord(columnTitle[i])-ord('A')+1
            r=r*26+a
        return r