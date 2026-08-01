class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # c=''
        # d=''
        # for i in word1:
        #     c+=i
        # for j in word2:
        #     d+=j
        # return c==d
        return ''.join(word1)==''.join(word2)