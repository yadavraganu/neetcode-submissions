class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        res = float('inf')
        
        while l < r:

            mid = l + (r-l)//2
            print(l,r,mid)

            if nums[mid] > nums [l]:
                res = min(nums[l],res)
                l = mid + 1
            else:
                res = min(nums[mid],res)
                r = mid
        
        return res
        