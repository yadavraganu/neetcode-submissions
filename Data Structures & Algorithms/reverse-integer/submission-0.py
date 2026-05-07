class Solution:
    def reverse(self, x: int) -> int:
        reverse_num  = 0
        int_max = (2**31) - 1
        int_min = -(2**-31)
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            a = x % 10
            reverse_num = reverse_num * 10 + a
            if ((reverse_num) // 10 > (int_max // 10)) or ((reverse_num // 10) == (int_max // 10) and (reverse_num % 10) > (int_max % 10)):
                return 0
            if (reverse_num // 10 < int_min // 10) or (reverse_num // 10 == int_min // 10 and reverse_num % 10 > int_min % 10):
                return 0
            x = x // 10
        return sign * reverse_num
