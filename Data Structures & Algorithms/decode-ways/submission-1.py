class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}

        def _helper(i):

            if i in memo:
                return memo[i]
            if i > len(s)-1:
                return 1
            if s[i] == '0':
                return 0
            
            res = _helper(i+1)

            if i+1 < len(s) and (s[i]=='1' or (s[i]=='2' and s[i+1] in '0123456')):
                res += _helper(i+2)
            
            memo[i] = res
            
            return res

        return _helper(0)
        