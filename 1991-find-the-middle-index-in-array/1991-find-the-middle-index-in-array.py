class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l=0
        s=sum(nums)
        for i in range(len(nums)):
            v=s-l-nums[i]
            if l==v:
                return i
            l+=nums[i]
        return -1