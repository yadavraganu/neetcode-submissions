class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        cnt_map = Counter(arr)
        res = -1
        for k,v in cnt_map.items():
            if k == v:
                res = max(res,k)
        return res
        