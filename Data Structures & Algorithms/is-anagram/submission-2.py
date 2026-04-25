class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)

        for k,v in counter_s.items():
            if counter_t.get(k,0) != v :
                return False
        return True        
        