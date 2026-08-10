class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)//2):
            print(nums[i],nums[-1-i])
            c+=int(str(nums[i])+str(nums[-1-i]))
        if len(nums)%2!=0:
            c+=nums[len(nums)//2]
        return c