class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def vow(a):
            c=0
            for i in a:
                if i in "aeiouAEIOU":
                    c+=1
            return c
        x=len(s)//2
        a=s[:x]
        b=s[x:]
        return vow(a)==vow(b)
