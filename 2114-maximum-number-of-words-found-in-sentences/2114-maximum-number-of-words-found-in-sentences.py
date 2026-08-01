class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c=[]
        for i in sentences:
            a=len(i.split())
            c.append(a)
        return max(c)