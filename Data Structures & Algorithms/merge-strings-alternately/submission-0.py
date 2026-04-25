class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        w1l = len(word1)
        w2l = len(word2)
        res = ''
        l1, l2 = 0, 0
        
        while l1 < w1l and l2 < w2l:
            res += word1[l1]
            res += word2[l2]
            l1 += 1
            l2 += 1

        if l1 < w1l:
            res += word1[l1:] 
    
        if l2 < w2l:
            res += word2[l2:]
        
        return res