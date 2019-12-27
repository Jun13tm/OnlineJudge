'''
    • Complexity: 
        ○ O(mnlog(mn)); O(mn)
    • Topics: 
        ○ dijkstra
Idea
好题，完完全全的dijkstra变体。（从找shortest path变成path with maximum minimum val），
感觉这题应该是hard才对。注意1 x 1 corner case
'''
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(A), len(A[0])
        
        # Use negative value for maxheap
        maxHeap = [(-A[0][0], 0, 0)]
        seen = [[0 for _ in range(C)] for _ in range(R)]
        while maxHeap:
            val, x, y = heapq.heappop(maxHeap)
            # seen[x][y] = 1 # got TLE
            if x == R - 1 and y == C - 1: return -val
            # Elegant
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and not seen[nx][ny]:
                    seen[nx][ny] = 1 # passed
                    heapq.heappush(maxHeap, (max(val, -A[nx][ny]), nx, ny))
        return -1
