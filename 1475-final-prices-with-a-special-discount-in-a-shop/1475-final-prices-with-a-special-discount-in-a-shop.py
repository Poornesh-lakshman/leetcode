class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        c=[]
        for i in range (len(prices)):
            for j in range (i+1,len(prices)):
                if prices[j]<=prices[i]:
                    c.append(prices[i]-prices[j])
                    break
            else:
                c.append(prices[i])
        return c