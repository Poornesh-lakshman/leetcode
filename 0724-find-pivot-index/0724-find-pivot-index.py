class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        s=sum(nums)
        for i in range(len(nums)):
            v=(s-left-nums[i])
            if left==v:
                return i
            left+=nums[i]
        return -1
