class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # return num in [6,28,496,8128,33550336]
        if num <= 1:
            return False
        c=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                c+=i
                if i*i!=num:
                    c+=num//i

        return c==num