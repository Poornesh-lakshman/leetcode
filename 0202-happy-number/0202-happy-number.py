class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def hap(n):
            b=0
            while(n>0):
                r=n%10
                b=b+r**2
                n//=10
            return b
        
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n=hap(n)
        return n==1