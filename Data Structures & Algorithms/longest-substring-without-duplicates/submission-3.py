class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash_map = {}
        res = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] not in hash_map:
                hash_map[s[r]] = 1
                r += 1
            else:
                hash_map[s[l]] -= 1
                if hash_map[s[l]] == 0:
                    del hash_map[s[l]]
                l += 1
            res = max(res,r-l)
        return res