class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        for i in nums:
            if i%2==0:
                a.append(i)
        d={}
        for i in a:
            d[i]=d.get(i,0)+1
        if not d:
            return -1
        ma=max(d.values())
        m=[key for key,values in d.items() if values==ma]
        return min(m)
        

