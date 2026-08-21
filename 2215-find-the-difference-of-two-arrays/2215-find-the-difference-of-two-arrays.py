class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # a=list(set(nums1))
        # b=list(set(nums2))
        # for i in a[:]:
        #     if i in b:
        #         a.remove(i)
        #         b.remove(i)
        # return [a,b]
        set1=set(nums1)
        set2=set(nums2)
        return [list(set1-set2),list(set2-set1)]