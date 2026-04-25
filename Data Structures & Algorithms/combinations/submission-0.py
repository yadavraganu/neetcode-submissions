class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = list(range(1,n+1))

        def _helper(idx,curr):
            
            if len(curr) == k:
                res.append(curr.copy())
                return
            if idx > n-1 :
                return
            curr.append(nums[idx])
            _helper(idx+1,curr)
            curr.pop()
            _helper(idx+1,curr)

        _helper(0,[])
        return res

        