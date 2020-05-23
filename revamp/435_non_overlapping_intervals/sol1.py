class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1: return 0
        
        # Sort by earliest end time
        intervals.sort(key=lambda x: x[1])
        end_time = intervals[0][1]
        count = 1
        
        # Arrange as many as possible
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end_time:
                end_time = intervals[i][1]
                count += 1
        return len(intervals) - count