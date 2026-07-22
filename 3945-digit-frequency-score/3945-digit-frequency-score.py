class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d={}
        a=[]
        for i in str(n):
            d[i]=d.get(i,0)+1
        for i in d.keys():
            a.append(int(i)*d[i])
        return sum(a)