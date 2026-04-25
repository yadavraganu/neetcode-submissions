class Solution:
    def numDecodings(self, s: str) -> int:

        def _helper(i):

            if i > len(s)-1:
                return 1
            if s[i] == '0':
                return 0
            
            res = _helper(i+1)

            if i+1 < len(s) and (s[i]=='1' or (s[i]=='2' and s[i+1] in '0123456')):
                res += _helper(i+2)
            
            return res

        return _helper(0)
        