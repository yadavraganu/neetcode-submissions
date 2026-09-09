class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l,r = 0 ,len(nums)-1
        t = 0

        while t <= r:
            if nums[t] != 0:
                nums[l] ,nums[t] = nums[t], nums[l]
                t += 1
                l += 1
            else:  
                t += 1 