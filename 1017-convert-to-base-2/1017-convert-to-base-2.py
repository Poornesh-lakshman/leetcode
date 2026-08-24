class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==0:
            return '0'
        a=''
        while n!=0:
            b=n%2
            a+=str(b)
            n=(n-b)//-2
        return a[::-1]