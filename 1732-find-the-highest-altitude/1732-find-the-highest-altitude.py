class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h=0
        l=[]
        l.append(h)
        for i in range(len(gain)):
            l.append(l[-1]+gain[i])
        
        return max(l)