class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_till_now = float('inf')
        max_profit = float('-inf')
        
        for i in range(len(prices)):
            min_till_now = min(min_till_now,prices[i])
            profit = prices[i] - min_till_now
            max_profit = max(max_profit,profit)
        return max_profit