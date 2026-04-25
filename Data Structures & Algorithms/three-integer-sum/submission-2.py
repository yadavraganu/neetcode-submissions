class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        def _helper(tgt , start_index):
             
            l = start_index
            r = len(nums) - 1

            if start_index > r:
                return False, l, r

            while l < r:
                sm = nums[l] + nums[r]
                if sm == tgt:
                    res.append((nums[l],nums[r],nums[i]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sm < tgt:
                    l += 1
                else:
                    r -= 1
            return False, l, r

        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            _helper(-1*nums[i],i+1)
        return res



        