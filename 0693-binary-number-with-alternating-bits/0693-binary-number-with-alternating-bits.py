class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        l=[]
        while n!=0:
            a=n%2
            l.append(a)
            n//=2
        for i in range(1,len(l)):
            if l[i-1]==l[i]:
                return False
        return True