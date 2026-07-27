class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        x=0
        for i in (arr1):
            valid=True
            for j in (arr2):
                if abs(i-j)<=d:
                    valid=False
                    break
            if valid:
                x+=1
        return x