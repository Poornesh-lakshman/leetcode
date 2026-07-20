class Solution:
    def mirrorDistance(self, n: int) -> int:
        b=n
        c=0
        while n!=0:
            a=n%10
            c=c*10+a
            print(c)
            n//=10
        
        return abs(b-c)