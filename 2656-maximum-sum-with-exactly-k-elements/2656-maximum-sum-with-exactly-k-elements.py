class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # d=0
        # for i in range(k):
        #     c=max(nums)
        #     nums.remove(c)
        #     nums.append(c+1)
        #     d+=c
        # return d
        max1=max(nums)
        d=0
        for i in range(k):
            d+=max1+i
        return d