class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        a=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            if j==1:
                a.append(i)
        return a