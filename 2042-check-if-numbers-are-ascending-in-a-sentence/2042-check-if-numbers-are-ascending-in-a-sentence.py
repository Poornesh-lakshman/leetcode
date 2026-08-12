class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.strip()
        a=-1
        for i in s.split():
            if i.isdigit():
                if int(i)<=a:
                    return False
                a=int(i)
        return True
