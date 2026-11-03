class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev_balloon = None
        res = 0
        temp_res = 0
        max_temp = 0
        for balloon, time in zip(colors,neededTime):
            if balloon != prev_balloon:
                res += temp_res - max_temp
                max_temp = 0
                temp_res = 0
            max_temp = max(max_temp,time)
            temp_res += time
            prev_balloon = balloon
        res += temp_res - max_temp
        return res
