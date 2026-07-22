class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        a=0
        b=1
        c=1
        for _ in range(2,n):
            a,b,c=b,c,a+b+c
        return c

