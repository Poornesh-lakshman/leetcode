class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        c=sorted(nums)
        return max(c[-3]*c[-2]*c[-1],c[0]*c[1]*c[-1])