class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if money - sum(prices[0:2]) < 0:
            return money
        else:
            return money - sum(prices[0:2])
