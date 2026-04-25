"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sorted_meets = sorted(intervals, key = lambda x : x.start )

        prev_meet_end = 0
        
        for meet in sorted_meets:
            j, k = meet.start, meet.end
            if j < prev_meet_end:
                return False
            prev_meet_end = k
        
        return True


