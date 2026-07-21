class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    #    one=0
    #    two=0
    #    for i in nums:
    #         one=(one^i)&~two
    #         two=(two^i)&~one
    #    return one

    
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            if j==1:
                return i