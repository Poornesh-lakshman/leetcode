class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        a=title.split()
        s=[]
        for i in a:
            if len(i)<=2:
                s.append(i.lower())
            else:
                s.append(i.title())
        return ' '.join(s)