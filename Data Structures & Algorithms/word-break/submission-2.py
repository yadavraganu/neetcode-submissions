class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hash_map = {}
        def traverse(i):
            res = []
            if i in hash_map:
                return hash_map[i]
            if i >= len(s):
                return True
            for word in wordDict:
                l = len(word)
                if s[i:i+l] == word:
                    res.append(traverse(i+l))
            result = any(res)
            hash_map[i] = result

            return result

        
        return traverse(0)