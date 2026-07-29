class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def traverse(i, cur_str):
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return
            for s in digitToChar[digits[i]]:
                cur_str += s
                traverse(i + 1, cur_str)
                cur_str = cur_str[:-1]

        if digits:
            traverse(0, "")
        return res
