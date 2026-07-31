class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d=['']*len(s)
        for i in range(len(s)):
            d[indices[i]]=s[i]
        return ''.join(d)
        
          