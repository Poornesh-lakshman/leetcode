class Solution:
    def areNumbersAscending(self, s: str) -> bool:
    
        a=-1
        for i in s.split():
            if i.isdigit():
                if int(i)<=a:
                    return False
                a=int(i)
        return True
