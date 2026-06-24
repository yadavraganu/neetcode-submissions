class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def gen(n):
            if n in [1,2]:
                return [1]*n
            prev = gen(n - 1)
            res = [1] + [0]*(n-2) + [1]
            for i in range(1,n-1):
                res[i] = prev[i-1] + prev[i]
            return res
        
        return [gen(i+1) for i in range(numRows)]
        