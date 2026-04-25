class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber > 0:
            columnNumber -= 1
            mod = columnNumber % 26
            div = columnNumber // 26
            res += chr(65 + mod)
            columnNumber = div
        return res[::-1]