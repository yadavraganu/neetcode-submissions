class Solution:
    def maxScore(self, s: str) -> int:
        from collections import Counter
        freq_map = Counter(s)
        zero = 0
        res = 0
        for i in s[:-1]:
            if i == '0':
                zero += 1
                temp_res = zero + freq_map['1']
            else:
                freq_map['1'] -= 1
            temp_res = zero + freq_map['1']
            res  = max(res,temp_res)
        return res