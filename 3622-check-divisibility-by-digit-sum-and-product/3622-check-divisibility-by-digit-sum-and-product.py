class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x=n
        b=0
        c=1
        while n:
            a=n%10
            b+=a
            c*=a
            n//=10
        return x%(b+c)==0