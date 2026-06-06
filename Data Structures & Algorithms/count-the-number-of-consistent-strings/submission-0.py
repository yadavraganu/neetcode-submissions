class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow_set = set(allowed)
        res = 0
        for word in words:
            curr_set = set(word)
            if len(curr_set - allow_set) == 0:
                res += 1
        return res
        