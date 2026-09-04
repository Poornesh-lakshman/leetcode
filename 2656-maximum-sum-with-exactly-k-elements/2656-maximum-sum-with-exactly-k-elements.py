class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max1=max(nums)
        d=0
        for i in range(k):
            d+=max1+i
        return d