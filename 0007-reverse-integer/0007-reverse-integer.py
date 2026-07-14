class Solution:
    def reverse(self, x: int) -> int:
        d=''
        i=0
        a=str(x)
        if a[i]=='-':
            d+=a[i]
            i+=1
        a=a[i::]
        z=int(d+a[::-1])
        if -2**31<= z <=2**31-1:
            return z
        else:
            return 0