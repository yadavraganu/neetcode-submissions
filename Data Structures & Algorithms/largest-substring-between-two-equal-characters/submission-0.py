class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mp = {}

        res = -1
        for i,v in enumerate(s):
            if v not in mp:
                mp[v] = i
            else:
                res = max(res,i-mp[v]-1)
        return res
        