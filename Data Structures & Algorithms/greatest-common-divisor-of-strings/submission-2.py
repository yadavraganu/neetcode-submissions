from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        common_len = gcd(len(str1), len(str2))
        candidate = str1[:common_len]
        return candidate