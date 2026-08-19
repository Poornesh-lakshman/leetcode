class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # c=''
        # for i in range (len(word)):
        #     c+=word[i]
        #     j=i
        #     if word[i]==ch:
        #         break
        # if ch not in word:
        #     return word
        # return c[::-1]+word[j+1::]
        if ch not in word:
             return word
        else:
            a= word.index(ch)
            return word[:a+1][::-1]+word[a+1:]