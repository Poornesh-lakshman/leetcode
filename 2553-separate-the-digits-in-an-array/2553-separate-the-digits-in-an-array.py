class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ab=[]
        for i in range(len(nums)):
            a=[]
            b=nums[i]
            while b>0:
                r=b%10
                a.append(r)
                b//=10
            a.reverse()
            ab.extend(a)
        return ab
        