class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        z=[]
        for i in range(left,right+1):
            n=i
            c=0
            d=len(str(n))
        
            
            while i>0:
                    r=i%10
                    if r==0:
                        break
                    else:
                        if n%r==0:
                            c+=1
                    i=i//10
            if c==d:
                    z.append(n)
        return z

        