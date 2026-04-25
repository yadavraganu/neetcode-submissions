class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h_map = {}

        for i ,j in enumerate(nums):
            if j in h_map:
                return [h_map[j],i]
            else:
                remaining = target - j
                h_map[remaining] = i    

        