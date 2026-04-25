class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        from math import sqrt

        heap = []

        for i in points:
            heapq.heappush(heap,(sqrt(i[0]**2+i[1]**2)*-1,i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]
        