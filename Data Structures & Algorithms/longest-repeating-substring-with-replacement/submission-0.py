class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hash_map = {}
        max_count_char = 0
        res = 0
        while r < len(s):
                hash_map[s[r]] = hash_map.get(s[r],0) + 1
                max_count_char = max(max_count_char,hash_map.get(s[r]))
                while ((r - l + 1) - max_count_char) > k:
                    hash_map[s[l]] -= 1
                    l += 1
                res = max(res,r - l + 1)
                r += 1
        return res



        