class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        b=[]
        while n>0:
            a=n%10
            b.append(a)
            n//=10
        c=0
        b=b[::-1]
        for i in range(len(b)):
            if i%2==0:
                c=c+b[i]
            else:
                c=c-b[i]
        return c
            
