class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums3=set(nums1).intersection(nums2)
        if nums3:
            return min(nums3)
        return -1
        # nums2=set(nums2)
        # nums3=set()
        # for i in set(nums1):
        #     if i in nums2:
        #         nums3.add(i)
        # if nums3:
        #    return min(nums3)
        # return -1