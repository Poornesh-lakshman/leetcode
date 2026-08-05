class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    c=(nums[j]-nums[i])
                    if c>ma:
                        ma=c
        return ma
      