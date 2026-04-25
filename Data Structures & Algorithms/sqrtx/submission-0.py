class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = None

        while l <= r:
            mid = l + ((r-l)//2)
            sqr = mid ** 2

            if sqr == x:
                return mid
            elif sqr < x:
                l  = mid + 1
                res = mid
            else:
                r = mid - 1
        return res
        