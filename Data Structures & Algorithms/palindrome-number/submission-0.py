class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new_num = 0
        old_num = x
        while old_num:
            new_num = (new_num*10) + (old_num % 10)
            old_num //= 10
        return x == new_num
        