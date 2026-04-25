class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hmap = set(nums)
        res = 0

        for i in nums:
            temp = i-1
            temp_res = 1
            while temp in hmap:
                temp_res += 1
                temp -= 1
            res = max(res,temp_res)
        return res

        