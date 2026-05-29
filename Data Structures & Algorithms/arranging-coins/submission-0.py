class Solution:
    def arrangeCoins(self, n: int) -> int:
        num = n
        i = 1
        res = 0
        while i <= n+1:
            if n >= i:
                res += 1
            n -= i
            i += 1
        return res


        