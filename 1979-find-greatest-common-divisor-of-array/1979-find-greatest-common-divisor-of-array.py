class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        c=[]
        for i in range(1,b+1):
            if a%i==0 and b%i==0:
                c.append(i)
        return max(c)
        