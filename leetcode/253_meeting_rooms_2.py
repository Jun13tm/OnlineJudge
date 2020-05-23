'''
    • Complexity: 
        ○ O(nlogn); O(n)
    • Topics: 
        ○ intervals
        ○ sort
Sort by starting time, then use min_heap to track ending time. The invarient
is, the size of min_heap is always equal to the minimum number of meeting rooms
needed at any index i.
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Edge case handling
        if not intervals: return 0
        
        # Sort by start time
        intervals.sort()
        
        # use min heap to track all allocated meeting room
        min_heap = []
        heapq.heappush(min_heap, intervals[0][1])
        for i in range(1, len(intervals)):
            heapq.heappush(min_heap, intervals[i][1])
            mi = min_heap[0]
            if intervals[i][0] >= mi:
                mi = heapq.heappop(min_heap)
        return len(min_heap) 