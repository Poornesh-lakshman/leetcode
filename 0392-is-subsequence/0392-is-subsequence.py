class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c=-1
        for i in s:
            if i in t:
                id=t.find(i,c+1)
                if id>=c:
                    c=id
                else:
                    return False
            else:
                return False
        return True