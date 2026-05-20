class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Edge case: no meetings
        if not intervals:
            return 0

        # Step 1: Separate start and end times into two lists
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        # Step 2: Use two pointers to traverse start and end times
        s_ptr, e_ptr = 0, 0
        used_rooms = 0
        max_rooms = 0

        # Step 3: Walk through all meetings by start times
        while s_ptr < len(starts):
            # If the current meeting starts before the earliest one ends,
            # we need a new room
            if starts[s_ptr] < ends[e_ptr]:
                used_rooms += 1
                max_rooms = max(max_rooms, used_rooms)
                s_ptr += 1
            else:
                # Otherwise, free up a room (move end pointer forward)
                used_rooms -= 1
                e_ptr += 1

        # Step 4: The maximum number of rooms used at any time is the answer
        return max_rooms
