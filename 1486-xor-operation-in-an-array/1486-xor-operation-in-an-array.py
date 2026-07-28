class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        y=0
        for i in range(n):
            y^=start+2*i
        return y
