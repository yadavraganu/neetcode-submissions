class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1_map, s2_map = [0]*26, [0]*26

        for i in range(len(s1)):
            print(i)
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if s1_map[i] == s2_map[i] else 0
        
        l, r = 0, len(s1)-1

        while r < len(s2)-1:

            if matches == 26:
                return True
            
            index_r = ord(s2[r+1]) - ord('a')
            
            s2_map[index_r] += 1
            if s2_map[index_r] == s1_map[index_r]:
                matches += 1
            if s2_map[index_r] - 1 == s1_map[index_r]:
                matches -= 1
            r += 1
            
            index_l = ord(s2[l]) - ord('a')
            
            s2_map[index_l] -= 1
            if s2_map[index_l] == s1_map[index_l]:
                matches += 1
            if s2_map[index_l] + 1 == s1_map[index_l]:
                matches -= 1
            l += 1
        return matches == 26
