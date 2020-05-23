'''
    • Complexity: 
        ○ O(mnlog(mn)); O(mn)
    • Topics: 
        ○ dijkstra
Idea
Dijsktra的核心在于找准greedy choice，传统dijsktra的bq pop出来的是当前与root距离最短的
node，此处pop出来的是距离root min value最大的coordinates。
注意从bq中pop出来即为visited（距root的最短距离found），之后不用再重新加入bq。而bq中也可能
同时存在多个相同的Node，但是和root间的距离不同。visit以后再被bq pop出来则直接跳过。
'''
import heapq

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        if not A or not A[0]: return 0
        
        r, c = len(A), len(A[0])
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[0 for _ in range(c)] for _ in range(r)]
        max_heap = [(-A[0][0], 0, 0)] # stores tuple: (-val, x, y)
        
        while max_heap:
            val, x, y = heapq.heappop(max_heap)
            # continue if visited
            if visited[x][y] == 0:
                if x == r - 1 and y == c - 1:
                    return -val
                visited[x][y] = 1
                for dx, dy in deltas:
                    x_, y_ = x + dx, y + dy
                    if 0 <= x_ < r and 0 <= y_ < c and visited[x_][y_] == 0:
                        heapq.heappush(max_heap, (max(val, -A[x_][y_]), x_, y_))
        # should not reach
        return -1