class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Edge case handling
        if not intervals: return 0

        # Sort all intervals by end time
        intervals.sort(key = lambda x: x[1])
        end_time = intervals[0][1]
        counter = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end_time:
                counter += 1
                end_time = intervals[i][1]
        return len(intervals) - counter