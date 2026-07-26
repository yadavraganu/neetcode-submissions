from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        q = deque()
        fresh = 0
        res = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1   

        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r1,c1 = q.popleft()

                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                
                for x,y in directions:
                    r2 = r1 + x
                    c2 = c1 + y 
                    if r2 in range(row) and c2 in range(col) and grid[r2][c2] == 1:
                        grid[r2][c2] = 2
                        fresh -= 1
                        q.append((r2,c2))
            res += 1
        return res if fresh == 0 else -1





        