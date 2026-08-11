class Solution:
    def replaceDigits(self, s: str) -> str:
        c=''
        for i in s:
            if i.isalpha():
                c+=i
                d=ord(i)
            else:
                c+=chr(d+int(i))
        return(c)