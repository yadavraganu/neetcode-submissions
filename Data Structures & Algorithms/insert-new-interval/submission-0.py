class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for idx, curr_interval in enumerate(intervals):
            if curr_interval[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[idx:]
            elif curr_interval[1] < newInterval[0]:
                res.append(curr_interval)
            else:
                newInterval = [min(curr_interval[0],newInterval[0]),max(curr_interval[1],newInterval[1])]
        res.append(newInterval)
        return res
