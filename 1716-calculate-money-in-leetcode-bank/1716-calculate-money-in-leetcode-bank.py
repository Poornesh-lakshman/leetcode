class Solution:
    def totalMoney(self, n: int) -> int:
        # a=0
        # z=0
        # c=0
        # d=1
        # for i in range(n):
        #     c+=1
        #     a+=1
        #     print(a,'a')
        #     if a==7:
        #         z+=c
        #         d+=1
        #         c=d-1
        #         a=0
        #     else:
        #         print(c)
        #         z+=c
        # return z

        total = 0
        monday = 1
        for i in range(n):
            day = i % 7
            total += monday + day
            if day == 6:
                monday += 1
        return total