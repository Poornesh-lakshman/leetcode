class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
            a=nums.index(pivot)
            l1=[]
            l2=[]
            l3=[]
            for i in range(len(nums)):
                if nums[i]<pivot:
                    l1.append(nums[i])
                elif nums[i]>pivot:
                    l2.append(nums[i])
                else:
                    l3.append(nums[i])
            return l1+l3+l2
            