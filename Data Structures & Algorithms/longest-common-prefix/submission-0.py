class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for index,st in enumerate(strs):

            j = 0
            
            while j < min(len(prefix),len(st)):
                
                if st[j] != prefix[j]:
                    break
                
                j += 1
            prefix = prefix[:j]
        
        return prefix