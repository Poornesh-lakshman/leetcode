class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l=-1
        for i in arr:
            if arr.count(i)==i:
                if i>l:
                    l=i
        return l