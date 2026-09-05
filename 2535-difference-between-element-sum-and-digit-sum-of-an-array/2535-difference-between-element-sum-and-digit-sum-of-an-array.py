class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        d=0
        for i in nums:
            while(i!=0):
                d+=i%10
                i//=10
        return sum(nums)-d
