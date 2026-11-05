class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        l_sum = 0
        r_sum = sum(nums)
        res = [] 

        for k, v in enumerate(nums):
            r_sum -= v
            temp = abs((r_sum - v*(len(nums)-k-1))) + abs((l_sum - v*k))
            res.append(temp)            
            l_sum += v 
        return res