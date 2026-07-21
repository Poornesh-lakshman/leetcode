class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a=bin(x^y)[2::]
        c=0
        for i in a:
            if i=='1':
                c+=1
        return c
        