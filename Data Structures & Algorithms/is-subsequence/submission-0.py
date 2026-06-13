class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        def traverse(i,j):
            if i == len(s):
                return True
            if j == len(t):
                return False
            if s[i] == t[j]:
                return traverse(i+1,j+1)
            else:
                return traverse(i,j+1)
        
        return traverse(0,0)