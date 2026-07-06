class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def ad(n):
            a=0
            while n>0:
                r=n%10
                a=a+r
                n//=10
            if a<=9:
                return a
            else:
                return ad(a)
        return ad(num)

        # while num>=10:
        #     sum=0
        #     for i in str(num):
        #         sum+=int(i)
        #         num=sum
        # return num