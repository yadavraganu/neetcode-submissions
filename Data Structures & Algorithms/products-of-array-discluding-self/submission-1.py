class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        prev = 1
        for i in range(len(nums)):
            arr[i] = prev
            prev = prev * nums[i]
        prev = 1
        for i in range(len(nums)-1,-1,-1):
            arr[i] *= prev
            prev = prev * nums[i]
        return arr