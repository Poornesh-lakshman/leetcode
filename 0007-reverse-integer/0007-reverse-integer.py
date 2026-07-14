class Solution:
    def reverse(self, x: int) -> int:
        # d=''
        # i=0
        # a=str(x)
        # if a[i]=='-':
        #     d+=a[i]
        #     i+=1
        # a=a[i::]
        # z=int(d+a[::-1])
        # if -2**31<= z <=2**31-1:
        #     return z
        # else:
        #     return 0

        sign=-1 if x<0 else 1
        x=abs(x)
        c=0
        while x!=0:
            a=x%10
            c=c*10+a
            x//=10
        sign*=c

        if sign >2**31-1 or sign<-2**31:
            return 0
         
        return sign