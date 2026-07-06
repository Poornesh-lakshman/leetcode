class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        a=''
        for i in range(len(s)):
            a=a+str(ord(s[i])-ord('a')+1)
        a=int(a)
        for i in range(k):
            b=0
            while a!=0:
                r=a%10
                b+=r
                a//=10
            a=b
        return b