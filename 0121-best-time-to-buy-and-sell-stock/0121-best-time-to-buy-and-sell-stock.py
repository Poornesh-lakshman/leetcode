class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m=prices[0]
        ma=0
        for i in prices:
            if i<m:
                m=i
            p=i-m
            if p>ma:
                ma=p
        return ma
