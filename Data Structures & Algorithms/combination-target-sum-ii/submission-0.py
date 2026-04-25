from typing import List


class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def _helper(i: int, tgt: int) -> None:
            if tgt == 0:
                res.append(subset.copy())
                return
            if tgt < 0 or i == len(nums):
                return

            subset.append(nums[i])
            _helper(i + 1, tgt - nums[i])

            next_i = i+1
            while next_i < len(nums) and nums[i] == nums[next_i]:
                next_i += 1 

            subset.pop()
            _helper(next_i, tgt)

        _helper(0, target)
        return res