class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d=len(set(candyType))
        e=len(candyType)/2
        if e<d:
            return int(e)
        else:
            return int(d)