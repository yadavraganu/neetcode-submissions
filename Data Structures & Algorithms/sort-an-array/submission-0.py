from collections import Counter
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Count Sort
        mn, mx = min(nums), max(nums)
        map = Counter(nums)
        idx = 0

        for i in range(mn, mx+1):
            while map[i] > 0:
                nums[idx] = i
                map[i] -= 1
                idx += 1
        
        return nums        

        