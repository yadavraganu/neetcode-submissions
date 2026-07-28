class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False

        tgt = sum(nums)/2
        dp = {}
        def traverse(i,s):
            if (i,s) in dp:
                return dp[(i,s)]
            elif s == tgt:
                return True
            elif i == len(nums):
                return False

            s += nums[i]
            res1 = traverse(i+1,s)
            s -= nums[i]
            res2 = traverse(i+1,s)
            dp[(i,s)] = res1 or res2
            return res1 or res2
        
        return traverse(0,0)

