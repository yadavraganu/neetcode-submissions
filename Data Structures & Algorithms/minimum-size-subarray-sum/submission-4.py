class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        for i in range(len(nums)):
            l, r = i, i
            temp_tgt = 0
            while temp_tgt < target and r <= len(nums)-1:
                temp_tgt += nums[r]
                r += 1
            if temp_tgt >= target:
                res = min(res,(r-l))
        return res if res != float("inf") else 0



        