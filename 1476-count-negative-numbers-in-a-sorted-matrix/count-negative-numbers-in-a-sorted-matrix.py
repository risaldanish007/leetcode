class Solution(object):
    def countNegatives(self, grid):
        negs = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    negs += 1
        return negs