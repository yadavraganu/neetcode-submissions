class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        res = []
        res.append(intervals[0])
        for start,end in intervals[1:]:
            prev_interval_end = res[-1][1]
            if start<=prev_interval_end:
                new_end = max(prev_interval_end,end)
                res[-1][1] =  new_end
            else:
                res.append([start,end])
        return res            

        