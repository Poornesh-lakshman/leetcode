class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def prime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        z=0

        for i in range(left,right+1):
            a=bin(i)[2:]
            c=0
            for j in a:
                if int(j)==1:
                    c+=1
            a=prime(c)
    
            if a:
                z+=1
        return z