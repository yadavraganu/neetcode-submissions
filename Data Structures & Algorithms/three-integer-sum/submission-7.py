class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, v in enumerate(nums):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            tgt = -1 * v
            l, r = i+1, len(nums)-1

            while l < r:
                sm = nums[l] + nums[r]
                if sm == tgt:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sm < tgt:
                    l += 1
                else:
                    r -= 1 
        return res