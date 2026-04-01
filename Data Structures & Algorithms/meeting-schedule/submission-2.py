"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        mins_list = []
        max_list = []
        for el in intervals:
            for i, val in enumerate(mins_list):
                if (el.start < max_list[i] and el.start >= mins_list[i]) or (el.end <= max_list[i] and el.end > mins_list[i]):
                    return False
            mins_list.append(el.start)
            max_list.append(el.end)
        return True