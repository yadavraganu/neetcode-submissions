class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0

        for i in range(len(nums)):
            if i<=maxJump:
                currJump = i + nums[i]
                maxJump = max(maxJump,currJump)
        
        return maxJump >= len(nums)-1