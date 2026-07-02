class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        a=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            if j>len(nums)/3:
                a.append(i)
        return a