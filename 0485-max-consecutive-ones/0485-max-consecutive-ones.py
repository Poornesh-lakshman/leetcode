class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l=[]
        c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                print(c)
            else:
                l.append(c)
                c=0
        l.append(c)
        return max(l)