class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        srtd_ip = sorted(intervals,key = lambda x : x[0])

        res = []
        prev = srtd_ip[0]
        
        for start, end in srtd_ip[1:]:
            if prev[1] < start:
                res.append(prev)
                prev = [start,end]
            else:
                prev = [prev[0],max(prev[1],end)]
        res.append(prev)     
        return res 
