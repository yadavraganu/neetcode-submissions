class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
    
        # Min-heap for Dijkstra (effort, row, col)
        heap = [(0, 0, 0)]
        
        # Effort matrix initialized to infinity
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        
        # Directions: up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            effort, r, c = heapq.heappop(heap)
            
            # If we reached bottom-right, return effort
            if r == rows - 1 and c == cols - 1:
                return effort
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Calculate effort for this move
                    next_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    
                    # If this path is better, update and push to heap
                    if next_effort < efforts[nr][nc]:
                        efforts[nr][nc] = next_effort
                        heapq.heappush(heap, (next_effort, nr, nc))