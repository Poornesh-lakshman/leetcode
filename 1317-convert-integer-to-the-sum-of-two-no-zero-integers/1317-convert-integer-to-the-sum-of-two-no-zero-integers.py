class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def nozero(n):
            return '0' not in str(n)
        for i in range(1,n):
            j=n-i
            if nozero(i) and nozero(j):
                return [i,j]