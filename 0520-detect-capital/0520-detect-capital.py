class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        a=[]
        a.append(word)
        if a[0].isupper() or a[0].islower() or a[0].istitle():
            return True
        else:
            return False