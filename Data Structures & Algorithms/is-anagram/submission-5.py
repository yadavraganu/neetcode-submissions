class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            arr[ord(s[i])-97] += 1
            arr[ord(t[i])-97] -= 1

        for i in arr:
            if i > 0:
                return False
        return True
        