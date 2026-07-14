class Solution:
    def myAtoi(self, s: str) -> int:
        c=''
        s=s.strip()
        i=0
        if i<len(s) and (s[i]=='+' or s[i]=='-'):
            c+=s[i]
            i+=1
        while i<len(s):
            if s[i].isdigit() :
                c=c+s[i]
            else:
                break
            i+=1
        if c=='' or c=='+' or c=='-':
            return 0
        
        c=int(c)
        if c>2**31-1:
            return 2**31-1
        elif c<-2**31:
            return -2**31
        else:
            return c