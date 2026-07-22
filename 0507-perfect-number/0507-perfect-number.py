class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in [6,28,496,8128,33550336]
        # c=0
        # for i in range(1,int(num//2)+1):
        #     if num%i==0:
        #         c+=i
        # return c==num