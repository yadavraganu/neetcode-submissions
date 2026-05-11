from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        Use two heaps:
        - min-heap (capital, profit) to track projects by required capital
        - max-heap (negative profit) to track affordable projects by profit (largest profit first)

        Algorithm:
        1. Push all (capital[i], profits[i]) into a min-heap by capital.
        2. For up to k times:
           - Move all projects with capital <= current w from min-heap to max-heap.
           - If max-heap is empty, break (no affordable projects left).
           - Pop the best affordable project (largest profit) and add its profit to w.
        3. Return the final capital w.
        """
        # Build a min-heap ordered by required capital: (capital, profit)
        cap_prof_min_heap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(cap_prof_min_heap)

        # Max-heap for affordable profits (store as negative to simulate max-heap)
        prof_max_heap = []

        for _ in range(k):
            # Move all affordable projects into the max-heap
            while cap_prof_min_heap and cap_prof_min_heap[0][0] <= w:
                c, p = heapq.heappop(cap_prof_min_heap)
                heapq.heappush(prof_max_heap, -p)  # negative for max-heap semantics

            # If there is no affordable project to pick, we cannot increase w further
            if not prof_max_heap:
                break

            # Pick the most profitable affordable project and add its profit to w
            w += -heapq.heappop(prof_max_heap)

        return w