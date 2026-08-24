class Solution:
    def convertToBase7(self, num: int) -> str:
        b=''
        if num==0:
            return '0'
        s=''
        if num<0:
            s='-'
            num=-num
        
        while num!=0:
            a=num%7
            b+=str(a)
            num//=7
        return s+b[::-1]