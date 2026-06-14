class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq_map = Counter(nums)
        nums.sort(key = lambda x : (freq_map[x],x*-1))
        return nums
        