class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        c=[]
        for i in range(1,arr[-1]):
            if i not in arr:
                c.append(i)
        if len(c)>=k:
            return c[k-1]
        return arr[-1]+(k-len(c))