class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mp = {}

        for i in arr:
            mp[i] = mp.get(i,0) + 1
        
        for i,j in mp.items():
            if j == 1:
                k -= 1
            if k == 0:
                return i
        return ""