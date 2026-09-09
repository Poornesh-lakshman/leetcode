class Solution:
    def isValid(self, s: str) -> bool:
        a={']':'[','}':'{',')':'('}
        l=[]
        if s[0] in '})]':
            return False
        for i in range(len(s)):
            if s[i] in '[{(':
                l.append(s[i])
            elif len(l)>0 and l[-1]==a[s[i]]:
                l.pop()
            else:
                return False
        return len(l)==0