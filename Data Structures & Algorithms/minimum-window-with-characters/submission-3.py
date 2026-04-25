class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t== '':
            return ''
 
        res = ''
        res_len = float('inf')
        from collections import Counter
        needed_map = Counter(t)
        needed_len = len(needed_map)
        current_len = 0
        current_map = {}
        l, r = 0, 0
        while r < len(s): 
            if s[r] in needed_map:
                current_map[s[r]] = current_map.get(s[r],0) + 1
            if s[r] in needed_map and needed_map[s[r]] == current_map[s[r]]:
                current_len += 1
            while current_len == needed_len:
                print(current_map,needed_map,l,r,res)
                if len(s[l:r+1]) < res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
                if s[l] in current_map:
                    current_map[s[l]] -= 1
                    if needed_map[s[l]] > current_map[s[l]]:
                        current_len -= 1
                    if current_map[s[l]] == 0:
                        del current_map[s[l]]
                l += 1   
            r += 1
        return res