from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        
        # Step 1: enqueue all treasures (0s) using for loops
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # Step 2: BFS traversal without for-loops, using direct +1/-1 offsets
        while q:
            r, c = q.popleft()
            
            # Down
            nr, nc = r + 1, c
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
            
            # Up
            nr, nc = r - 1, c
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
            
            # Right
            nr, nc = r, c + 1
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
            
            # Left
            nr, nc = r, c - 1
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
