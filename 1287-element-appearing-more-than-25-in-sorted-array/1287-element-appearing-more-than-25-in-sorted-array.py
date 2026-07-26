class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d={}
        l=[]
        x=len(arr)//4
        for i in arr:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            if j>x:
                l.append(i)
        return max(l)