class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # edge case handling
        if len(intervals) <= 1: return intervals
        
        # sort by starting time
        intervals.sort()
        ret = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ret[-1][1]:
                prev = ret.pop()
                merged = [prev[0], max(intervals[i][1], prev[1])]
                ret.append(merged)
            else:
                ret.append(intervals[i])
        return ret