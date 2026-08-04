class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        st=sum(nums[:k])
        ma=st
        for i in range(k,len(nums)):
            st+=nums[i]-nums[i-k]
            ma=max(ma,st)
        return ma/k