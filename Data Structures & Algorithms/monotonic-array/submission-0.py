class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if len(nums) <= 2:
            return True

        max_till_now = max(nums[0],nums[1])
        mono_incr = True
        mono_decr = True

        for i in range(1,len(nums)):

            if nums[i] <  nums[i-1]:
                mono_incr = False

            if nums[i] >  nums[i-1]:
                mono_decr = False

        return mono_incr or mono_decr