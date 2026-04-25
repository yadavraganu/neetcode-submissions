class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        for k, v in Counter(nums).items():
            if v > len(nums)/2:
                return k
        