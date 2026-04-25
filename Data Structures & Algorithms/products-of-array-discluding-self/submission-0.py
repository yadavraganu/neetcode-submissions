class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l_sum=[1] * len(nums)
        r_sum=[1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                product = 1
            else:    
                product = product * nums[i-1]    
            l_sum[i]=product
    
        for j in range(len(nums)-1,-1,-1):
            if j == len(nums)-1:
                product = 1
            else:    
                product = product * nums[j+1]
            print(j,product)    
            r_sum[j] = product        
        
        res = []
        for i in range(len(l_sum)):
            summ = l_sum[i]*r_sum[i]
            res.append(summ)
        return res    
