class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # d=['']*len(s)
        # for i in range(len(s)):
        #     d[indices[i]]=s[i]
        # return ''.join(d)
        
        a=dict(zip(indices,s))
        b=sorted(indices)
        d=''
        for i in b:
            d+=a[i]
        return d

          