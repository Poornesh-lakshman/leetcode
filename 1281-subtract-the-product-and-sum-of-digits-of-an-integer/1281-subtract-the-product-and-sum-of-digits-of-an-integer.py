class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=n
        c=0
        d=1
        while n!=0:
            b=n%10
            c+=b
            d*=b
            n//=10
        return d-c