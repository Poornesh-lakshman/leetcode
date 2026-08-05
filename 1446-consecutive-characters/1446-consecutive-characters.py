class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=s[0]
        c=1
        v=[]
        for i in range(1,len(s)):
            if a==s[i]:
                c+=1
                
            else:
                v.append(c)
                c=1
            a=s[i]
        v.append(c)
        return max(v)
