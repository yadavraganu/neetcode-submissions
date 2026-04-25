class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        maper = {}
        def climb(i):

            if i in maper:
                return maper[i]

            if i >= len(cost):
                return 0
            
            min_cost_1 = cost[i] + climb(i+1)
            min_cost_2 = cost[i] + climb(i+2)
            maper[i] = min(min_cost_1,min_cost_2)
            return maper[i]

        return min(climb(0) , climb(1))

        