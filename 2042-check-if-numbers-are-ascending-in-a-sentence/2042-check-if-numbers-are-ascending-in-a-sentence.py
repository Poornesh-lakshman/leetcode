class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.split()
        c=0
        for i in s:
            if i.isdigit():
                m=int(i)
                if m>c:
                    c=m
                    continue
                else:
                    return(False)
        return(True)