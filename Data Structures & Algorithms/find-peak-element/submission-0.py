class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = left + (right - left) // 2
            
            # If climbing up, the peak is to the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # If walking down, the peak is at mid or to the left
            else:
                right = mid
                
        return left
        