class Solution:
    def maxProduct(self, n: int) -> int:
        l=list(str(n))
        n=sorted(l)
        return int(n[-1])*int(n[-2])
        