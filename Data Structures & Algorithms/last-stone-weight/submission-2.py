class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        max_heap = []
        for i in stones:
            heapq.heappush(max_heap,-i)
        
        while len(max_heap)>1:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            heapq.heappush(max_heap,first-second)
        return abs(max_heap[0])