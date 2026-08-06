class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        
        while True:
            c=1
            for i in str(n):
                c*=int(i)
            if c%t==0:
                return n
            n+=1                

        