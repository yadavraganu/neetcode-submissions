import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Count frequencies of each task
        counts = Counter(tasks)
        
        # 2. Build Max-Heap (Python has min-heap, so we use negative values)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        
        # 3. Queue to store tasks cooling down: [remaining_count, available_time]
        cooldown_queue = deque()
        
        while max_heap or cooldown_queue:
            time += 1
            
            if max_heap:
                # Execute the most frequent available task
                count = heapq.heappop(max_heap) + 1  # +1 because it's negative
                
                # If the task still has instances left, put it in cooldown
                if count != 0:
                    cooldown_queue.append((count, time + n))
            
            # 4. Check if any task has finished its cooldown
            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(max_heap, cooldown_queue.popleft()[0])
            
        return time