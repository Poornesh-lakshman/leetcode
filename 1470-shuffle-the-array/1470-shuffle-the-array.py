class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=len(nums)//2
        l=[]
        for i in range(a):
            l.append(nums[i])
            l.append(nums[a])
            a+=1
        return l
