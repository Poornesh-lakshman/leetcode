class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        h=len(s)-1
        s=list(s)
        v='aeiouAEIOU'
        while l<h:
            if s[l] in v and s[h] in v:
                s[l],s[h]=s[h],s[l]
                l+=1
                h-=1
            elif s[l] not in v and s[h] in v:
                l+=1
            else:
                h-=1
        return ''.join(s)