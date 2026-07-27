class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l=[]
        for i in arr:
            if arr.count(i)==i:
                l.append(i)
        if len(l)>0:
            return max(l)
        else:
            return -1