import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Edge case: no meetings
        if not intervals:
            return 0

        # Step 1: Sort all meetings by their start time
        intervals.sort(key=lambda x: x.start)

        # Step 2: Initialize a min-heap to track end times of ongoing meetings
        # Push the end time of the first meeting
        min_heap = [intervals[0].end]

        # Step 3: Process the rest of the meetings
        for interval in intervals[1:]:
            # If the earliest ending meeting finishes before the current one starts,
            # we can reuse that room (pop from heap)
            if interval.start >= min_heap[0]:
                heapq.heappop(min_heap)

            # Push the current meeting's end time into the heap
            # (either reusing a room or allocating a new one)
            heapq.heappush(min_heap, interval.end)

        # Step 4: The number of rooms required is the size of the heap
        return len(min_heap)
