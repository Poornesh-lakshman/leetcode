class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        d={}
        c=[]
        s1=s1+' '+s2
        for i in s1.split():
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            if j==1:
                c.append(i)
        return c