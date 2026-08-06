class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=nums[0]
        r=-1
        for i in range(1,len(nums)):
            if nums[i]>a:
                r=max(r,nums[i]-a)
            else:
                a=nums[i]
        return r