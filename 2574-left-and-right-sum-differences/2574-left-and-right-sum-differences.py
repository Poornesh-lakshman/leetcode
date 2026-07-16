class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # s=sum(nums)
        # left=0
        # z=[]
        # for i in range(len(nums)):
        #     x=abs(left-(s-left-nums[i]))
        #     left+=nums[i]
        #     z.append(x)
        # return z

        z=[]
        for i in range(len(nums)):
            x=abs(sum(nums[:i])-sum(nums[i+1:]))
            z.append(x)
        return z