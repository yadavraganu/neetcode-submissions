class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        rightSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum -= nums[i]
            if i > 0:
                leftSum += nums[i-1]
            if leftSum == rightSum:
                return i
        return -1
        