class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # c=-1
        # for i in s:
        #     if i in t:
        #         id=t.find(i,c+1)
        #         if id>=c:
        #             c=id
        #         else:
        #             return False
        #     else:
        #         return False
        # return True

        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)