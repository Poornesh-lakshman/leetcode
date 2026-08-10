class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # a=0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j]<0:
        #             a+=1
        # return a
        count=0
        for li in grid:
            count+=len([i for i in li if i<0])
        return count
