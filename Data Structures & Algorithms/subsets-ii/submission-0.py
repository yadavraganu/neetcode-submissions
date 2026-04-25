class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def _helper(idx,subset):
            if idx == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[idx])
            _helper(idx+1,subset)
            subset.pop()

            next_idx = idx+1
            while next_idx < len(nums) and nums[next_idx] == nums[next_idx-1]:
                next_idx += 1

            _helper(next_idx,subset)

        _helper(0,[])
        return res