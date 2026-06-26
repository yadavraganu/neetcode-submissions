from typing import List
from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = float('inf')

        @lru_cache(None)
        def _helper(tgt: int, no_of_coins: int) -> None:
            nonlocal res
            if tgt == 0:
                res = min(no_of_coins, res)
                return

            for coin in coins:
                if tgt - coin >= 0:
                    _helper(tgt - coin, no_of_coins + 1)

        _helper(amount, 0)
        return -1 if res == float('inf') else res
