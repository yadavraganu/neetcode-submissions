class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        hash_map = Counter(nums)
        min_heap = []
        for i in hash_map.keys():
            heapq.heappush(min_heap,(hash_map[i],i))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [heapq.heappop(min_heap)[1] for i in range(k)]



        