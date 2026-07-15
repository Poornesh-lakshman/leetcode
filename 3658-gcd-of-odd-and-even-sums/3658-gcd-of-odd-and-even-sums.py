class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        a=1
        b=0
        c=0
        d=n
        while n!=0 and d!=0:
            if a%2==0:
                b+=a
                n-=1
            else:
                c+=a
                d-=1
            a+=1
        return c-b
            