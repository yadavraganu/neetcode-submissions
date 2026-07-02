class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i, j):

            if (i,j) in dp:
                return dp[(i,j)]

            if i == len(nums):
                return 0

            LIS = dfs(i + 1, j) # not include

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i)) # include
            dp[(i,j)] = LIS
            return LIS

        return dfs(0, -1)