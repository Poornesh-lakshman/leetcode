class Solution:
    def numberOfMatches(self, n: int) -> int:
        # b,c=0,0
        # while n>1:
        #     if n%2==0:
        #         n=n/2
        #         b+=n
        #     else:
        #         a=(n-1)/2
        #         n=n-a
        #         c+=a
        # return int(b+c)
        return n-1
            

