class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c=0
        for i in sentences:
            a=len(i.split())
            if a>c:
                c=a
        return c