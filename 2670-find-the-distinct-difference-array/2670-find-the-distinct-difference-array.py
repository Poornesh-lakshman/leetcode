class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        z=[]
       
        for i in range(len(nums)):
            a=len(set(nums[i+1:]))
            b=len(set(nums[:i+1]))
            z.append(b-a)
        return z