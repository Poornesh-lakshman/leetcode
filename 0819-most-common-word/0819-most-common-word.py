class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        d={}
        pa=re.findall(r'\w+', paragraph.lower())
        for i in pa:
            if i not in banned:
                d[i]=d.get(i,0)+1
        a=max(d,key=d.get)
        return a