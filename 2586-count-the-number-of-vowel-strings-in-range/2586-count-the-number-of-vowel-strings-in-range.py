class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        c=0
        for i in range(left,right+1):
            a=words[i]
            if a[0] in 'aeiouAEIOU' and a[-1] in 'aeiouAEIOU':
                c+=1
        return c