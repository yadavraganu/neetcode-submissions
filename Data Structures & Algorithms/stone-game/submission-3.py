class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dfs(l, r):
            if (l,r) in memo:
                return memo[(l,r)]
            if l > r:
                return 0
            res = max(dfs(l + 1, r) + piles[l], dfs(l, r - 1) + piles[r])
            memo[(l,r)] = res
            return res

        total = sum(piles)
        alice_score = dfs(0, len(piles) - 1)
        return alice_score > total - alice_score