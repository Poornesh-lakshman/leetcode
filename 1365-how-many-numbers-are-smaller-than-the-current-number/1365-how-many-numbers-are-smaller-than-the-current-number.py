class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        c=0
        for i in nums:
            for j in nums:
                if i>j :
                    c+=1
            l.append(c)
            c=0
        return l