class Solution:
    def reverseWords(self, s: str) -> str:
        v=[]
        for i in s.split():
            v.append(i[::-1])
        return ' '.join(v)