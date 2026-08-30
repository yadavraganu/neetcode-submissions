class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev = 0 
        res = 0
        curr_sum = 0
        for num in nums:
            if prev < num:
                curr_sum += num
            else:
                curr_sum = num
            res = max(res,curr_sum)
            prev = num
        return res

        