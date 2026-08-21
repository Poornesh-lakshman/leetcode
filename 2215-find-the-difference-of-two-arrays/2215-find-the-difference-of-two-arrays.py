class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=list(set(nums1))
        b=list(set(nums2))
        c=[]
        for i in a[:]:
            if i in b:
                a.remove(i)
                b.remove(i)
        c.append(a)
        c.append(b)
        return c