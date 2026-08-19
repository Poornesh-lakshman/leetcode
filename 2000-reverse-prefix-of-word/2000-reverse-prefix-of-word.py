class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        c=''
        for i in range (len(word)):
            c+=word[i]
            j=i
            if word[i]==ch:
                break
        if ch not in word:
            return word
        return c[::-1]+word[j+1::]