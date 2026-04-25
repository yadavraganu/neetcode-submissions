class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_k = max(piles)
        min_k = 1
        res = max_k

        while min_k <= max_k:
            mid_k = (min_k + max_k) // 2
            timeTaken = 0
            for p in piles:
                timeTaken += math.ceil(float(p) / mid_k)
            if timeTaken <= h:
                res = mid_k
                max_k = mid_k - 1
            else:
                min_k = mid_k + 1
        return res