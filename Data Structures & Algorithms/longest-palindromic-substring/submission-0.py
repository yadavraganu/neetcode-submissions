class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPali(s,l,r):
            res = ''
            while l <= r and l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l)+1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
            return res
        res = ''
        for i in range(len(s)):

            res1 = isPali(s,i,i)
            res2 = isPali(s,i,i+1)

            res = res1 if len(res1) > len(res) else res
            res = res2 if len(res2) > len(res) else res
        
        return res