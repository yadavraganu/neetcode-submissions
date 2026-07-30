import heapq
from typing import List

class Solution:
    def mostBooked(self, num_rooms: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()

        available_rooms = []  # min-heap of available room indices
        ongoing_meetings = []  # min-heap of (end_time, room_index)
        meeting_count_per_room = [0] * num_rooms

        # Initialize all rooms as available
        for room_index in range(num_rooms):
            heapq.heappush(available_rooms, room_index)

        for start_time, end_time in meetings:
            # Free all rooms that have finished before current meeting starts
            while ongoing_meetings and ongoing_meetings[0][0] <= start_time:
                finished_end_time, finished_room = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, finished_room)

            # If no room is available, delay meeting until earliest room frees up
            if not available_rooms:
                earliest_end_time, occupied_room = heapq.heappop(ongoing_meetings)
                adjusted_end_time = earliest_end_time + (end_time - start_time)
                heapq.heappush(available_rooms, occupied_room)
                end_time = adjusted_end_time

            # Assign meeting to the smallest available room
            assigned_room = heapq.heappop(available_rooms)
            heapq.heappush(ongoing_meetings, (end_time, assigned_room))
            meeting_count_per_room[assigned_room] += 1

        # Return the room with the maximum number of meetings
        return meeting_count_per_room.index(max(meeting_count_per_room))
