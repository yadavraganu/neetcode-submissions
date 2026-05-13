class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        curr_min = 1
        curr_max = 1
        for i in nums:
            temp = i * curr_max
            curr_max = max(i * curr_max,i * curr_min, i)
            curr_min = min(temp,i * curr_min, i)
            res = max(res,curr_max)
        return res