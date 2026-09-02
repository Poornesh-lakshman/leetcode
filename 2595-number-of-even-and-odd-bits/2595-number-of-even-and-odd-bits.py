class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        c=''
        while n>0:
            a=n%2
            c+=str(a)
            n//=2
        d,e=0,0
        for i in range(len(c)):
            if c[i]=='1':
                if i%2==0:
                    d+=1
                else:
                    e+=1
        return [d,e]
        