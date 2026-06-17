class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(set(s.split())) != len(set(pattern)) or len(s.split()) != len(pattern):
            return False
        arr = s.split()
        s_map = dict()
        for i in range(len(arr)):
            if arr[i] not in s_map:
                s_map[arr[i]] = pattern[i]
            else:
                if s_map[arr[i]] != pattern[i]:
                    return False
        return True
        