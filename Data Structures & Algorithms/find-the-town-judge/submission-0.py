class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        from collections import defaultdict
        trust_map_1 = defaultdict(list)
        trust_map_2 = defaultdict(list)

        for trustee, trusted in trust:
                trust_map_1[trusted].append(trustee)
                trust_map_2[trustee].append(trusted)

        for i in range(1,n+1):
            if len(trust_map_2[i]) == 0 and len(trust_map_1[i])== n-1:
                return i
        return -1