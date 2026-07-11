class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def traverse(i,j):
            if (i,j) in  dp:
                return dp[(i,j)]
            elif i == m-1 and j == n-1:
                return 1
            elif i >= m or j >= n:
                return 0
            else:
                dp[(i,j)] = traverse(i+1,j) + traverse(i,j+1)
                return dp[(i,j)]
        return traverse(0,0) 
        