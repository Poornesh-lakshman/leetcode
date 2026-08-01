class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        c=[]
        for i in range(len(nums)):
            if target==nums[i]:
                c.append(i)
        return c