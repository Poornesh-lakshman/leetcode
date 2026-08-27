class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        # c=s.count(letter)
        # return int(c/len(s)*100)
        count=0
        percent=0
        n=len(s)
        for char in s:
            if char==letter:
                count+=1
        percent=(count*100)//n
        return percent