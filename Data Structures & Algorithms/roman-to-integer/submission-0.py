class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        prev = None
        map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        for i in range(len(s)-1,-1,-1):
            if prev is None or prev <= map[s[i]]:
                res += map[s[i]]
            else:
                res -= map[s[i]]
            prev = map[s[i]]
        return res