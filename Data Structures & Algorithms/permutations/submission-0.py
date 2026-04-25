class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        
        def _helper(subset):

            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in subset:
                    subset.append(nums[i])
                    _helper(subset)
                    subset.pop()
        
        _helper([])
        return res



