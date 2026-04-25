class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map ={}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                entry = target-nums[i]
                hash_map[entry] = i
            else:
                return [hash_map[nums[i]],i]


        