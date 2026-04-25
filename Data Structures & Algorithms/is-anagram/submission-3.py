class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        from collections import Counter
        
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False

        s_map = Counter(s)

        for i in t:
            s_map[i] = s_map[i] - 1
            if s_map[i] == 0:
                del s_map[i]
        
        if s_map:
            return False
        
        return True