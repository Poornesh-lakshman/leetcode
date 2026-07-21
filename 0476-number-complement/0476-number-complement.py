class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a=bin(num)[2::]
        c=''
        for i in a:
            if i=='1':
                c+='0'
            else:
                c+='1'
        return int(c,2)