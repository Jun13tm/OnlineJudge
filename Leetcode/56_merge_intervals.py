'''
92: Reverse Linked List 2 Medium 
    • Complexity:
        ○ O(n); O(1)
    • Topics:
        ○ intervals
        ○ sort
sort by start time确保新的interval只需要和前一个interval比较，guarantee与前一个以前的
interval都不会overlap。
'''
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