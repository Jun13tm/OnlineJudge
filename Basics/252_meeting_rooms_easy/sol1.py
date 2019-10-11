class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1: return True
                
        # Sort by start time
        intervals.sort()
        end_time = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < end_time: return False
            end_time = max(intervals[i][1], end_time)
        return True