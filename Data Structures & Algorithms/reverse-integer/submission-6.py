class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31
        MAX = 2147483647   #  2^31 - 1

        sign = -1 if x < 0 else 1
        res = 0
        while x != 0:
            digit = abs(x) % 10 
            x = int(abs(x) / 10)

            # Positive overflow check
            if sign*res > int(MAX / 10) or (sign*res == int(MAX / 10) and digit > 7):
                return 0
            # Negative overflow check
            if sign*res < int(MIN / 10) or (sign*res == int(MIN / 10) and digit < -8):
                return 0

            res = res * 10 + digit

        return sign*res
