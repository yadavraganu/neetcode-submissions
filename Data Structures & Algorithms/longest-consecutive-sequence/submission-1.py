class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        hash_set = set(nums)
        
        for i, j in enumerate(nums):
            temp = j - 1
            ln = 1
            while temp in hash_set:
                ln += 1
                temp -= 1
            res = max(res,ln)
        return res
        