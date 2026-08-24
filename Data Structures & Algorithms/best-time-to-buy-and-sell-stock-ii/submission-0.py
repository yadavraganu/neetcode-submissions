class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        running_min = prices[0]
        profit = 0

        for price in prices:
            curr_profit = price-running_min
            print(curr_profit,running_min)
            if curr_profit > 0:
                profit += curr_profit
                running_min = price
            running_min = min(running_min,price)

        return profit