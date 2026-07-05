class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i,skip):
            if (i,skip) in dp:
                return dp[(i,skip)]

            if i >=len(nums) or (skip and  i == len(nums)-1):
                return 0
            
            res1 = dfs(i+1,skip)
            if i == 0:
                skip = True
            res2 = nums[i] + dfs(i+2,skip)
            dp[(i,skip)] = max(res1,res2)
            return max(res1,res2)
        
        return dfs(0,False)