class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    c.append(nums[j]-nums[i])
        if c==[]:
            return -1
        return max(c)