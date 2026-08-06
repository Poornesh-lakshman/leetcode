class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c=0
        a='aeiou'
        for i in range(k):
            if s[i] in a:
                c+=1
        ma=c
        for i in range(k,len(s)):
            if s[i] in a:
                c+=1
            if s[i-k] in a:
                c-=1
            ma=max(ma,c)
        return ma

            
            