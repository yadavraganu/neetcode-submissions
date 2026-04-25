class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        member_arr = [False]*len(nums)

        def _helper(subset):
            
            if len(subset) == len(nums):
                result.append(subset.copy())
                return
            
            for k, v in enumerate(nums):
                if member_arr[k] or (k > 0 and nums[k] == nums[k-1] and not member_arr[k-1]):
                    continue
                subset.append(v)
                member_arr[k] = True
                _helper(subset)
                subset.pop()
                member_arr[k] = False
        nums.sort()
        _helper([])

        return result
            