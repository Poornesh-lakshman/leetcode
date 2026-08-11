class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        c=0
        d=0
        ma=0
        mx=0
        for i in s:
            if i=='1':
                c+=1
                d=0
                if ma<c:
                    ma=c
            else:
                d+=1
                c=0
                if mx<d:
                    mx=d
        if ma>mx:
            return(True)
        return (False)