class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = {}

        def traverse(l,m):

            if (l,m) in dp:
                return dp[(l,m)]
            
            if l == row or col == m or obstacleGrid[l][m] == 1:
                return 0
            
            if (l,m) == (row-1,col-1):
                return 1
            
            dp[(l,m)] = traverse(l+1,m) + traverse(l,m+1)
            
            return dp[(l,m)]

        return traverse(0, 0)
        