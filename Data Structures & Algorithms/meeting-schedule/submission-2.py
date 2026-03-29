"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.end)
        i = 0
        while (i+1 <= len(intervals) - 1):
            if intervals[i+1].start < intervals[i].end:
                return False 
            i += 1
        
        return True
