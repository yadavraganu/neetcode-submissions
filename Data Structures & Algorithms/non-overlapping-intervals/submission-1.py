class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals by their end time
        srtd_ip = sorted(intervals, key=lambda x: x[1])

        res = 0  # Counter for number of intervals removed
        prevEnd = float('-inf')  # Track the end of the last non-overlapping interval
        
        # Step 2: Iterate through each interval
        for start, end in srtd_ip:
            if prevEnd <= start:
                # Case A: No overlap → keep this interval
                prevEnd = end
            else:
                # Case B: Overlap detected → remove one interval
                res += 1
        
        # Step 3: Return the total number of removals
        return res
