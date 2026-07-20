class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a=(bin(n)[2::])
        c=''
        for i in a:
            if i=='1':
                c+='0'
            else:
                c+='1'
        return (int(c,2))
