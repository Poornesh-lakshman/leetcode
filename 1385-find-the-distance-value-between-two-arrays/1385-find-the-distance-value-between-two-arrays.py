class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        x=0
        for i in range(len(arr1)):
            valid=True
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    valid=False
                    break
            if valid:
                x+=1
            
        return x