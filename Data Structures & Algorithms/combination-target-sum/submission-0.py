class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def _helper(i,tgt):

            if 0 == tgt:
                res.append(subset.copy())
                return
            
            if tgt < 0 or i == len(nums):
                return

            subset.append(nums[i])
            _helper(i,tgt-nums[i])
            subset.pop()
            _helper(i+1,tgt)
                
        _helper(0,target)

        return res        