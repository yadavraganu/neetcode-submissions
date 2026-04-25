class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def traverse(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:  # already visited
                return 0
            grid[r][c] = -1
            res = traverse(r+1,c) + traverse(r-1,c) + traverse(r,c+1) + traverse(r,c-1)
            return res

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return traverse(row,col)