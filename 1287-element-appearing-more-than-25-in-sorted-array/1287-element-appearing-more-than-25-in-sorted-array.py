class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d={}
        l=[]
        for i in arr:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            if j>len(arr)//4:
                l.append(i)
        return max(l)