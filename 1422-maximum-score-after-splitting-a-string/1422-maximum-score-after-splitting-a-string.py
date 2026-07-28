class Solution:
    def maxScore(self, s: str) -> int:
        c=''
        l=[]
        for i in range(len(s)-1):
            c+=s[i]
            x=c.count('0')
            d=s[i+1::]
            y=d.count('1')
            l.append(x+y)
        return (max(l))
            