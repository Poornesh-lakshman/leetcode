class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        c=[]
        for i in nums1:
            if i in nums2:
                c.append(i)
        if c:
            return min(c)
        a= min(nums1) 
        b= min(nums2)
        if a<b:
            return int(str(a)+str(b))
        return int(str(b)+str(a))
