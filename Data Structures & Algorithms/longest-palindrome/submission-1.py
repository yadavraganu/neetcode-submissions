from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        odd_found = False
        
        for freq in count.values():
            res += freq // 2 * 2
            if freq % 2 == 1:
                odd_found = True
        
        return res + (1 if odd_found else 0)
