class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_distance = nums[-1] - nums[0]
        low = 0
        high = max_distance
        while low <= high:
            mid = low + (high-low)//2

            l = 0
            r = 0
            count = 0

            while r < len(nums):

                while nums[r] - nums[l] > mid:
                    l += 1

                count += r - l
                r += 1
            if count >= k:
                high = mid - 1
            else:
                low = mid + 1
        return low