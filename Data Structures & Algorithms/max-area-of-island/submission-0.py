class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        res = 0
        def traverse(r,c):
            if r == row or c == col or r < 0 or c < 0 or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            left = traverse(r, c+1)
            right = traverse(r, c-1)
            up = traverse(r-1, c)
            down = traverse(r+1, c)
            return grid[r][c]+left+right+up+down
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    temp = traverse(i,j)
                    res = max(res,temp)
        return res
