class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # return(abs((nums.index(target)-start))
        a=[]
        for i in range(len(nums)):
            if target==nums[i]:
                a.append(abs(i-start))
        return min(a)
        