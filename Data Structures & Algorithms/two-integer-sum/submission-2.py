class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i, j in enumerate(nums):
            rem = target - j
            if j in hash_map:
                return [hash_map[j],i]
            hash_map[rem] = i