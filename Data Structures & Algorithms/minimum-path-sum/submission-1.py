class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        row = len(grid)
        col = len(grid[0])
        def traverse(m,n):
            if (m,n) in dp:
                return dp[(m,n)]
            if m == row or n == col or m < 0 or n < 0:
                return float('inf')
            
            if m == row-1 and n == col-1:
                return grid[m][n]

            right = traverse(m,n+1)
            down = traverse(m+1,n)
            dp[(m,n)] = min(right,down)+grid[m][n]
            return dp[(m,n)]
        return traverse(0,0)
        