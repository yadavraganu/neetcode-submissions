class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rng = len(nums)
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                continue
            else:
                nums[num-1] *= -1
        res = []
        for i,num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        return res