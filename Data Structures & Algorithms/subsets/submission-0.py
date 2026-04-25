class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def _helper(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            _helper(i+1)
            subset.pop()
            _helper(i+1)
        
        _helper(0)
        return res
        