'''
1135: Connecting Cities with Minimum Cost Medium 
    • Complexity:
        ○ O(nlogn)
    • Topics:
        ○ heaq
        ○ bfs
目标是找到把所有城市connect所需要的最短距离 -> greedy approach。永远pop最短的edge，如果
该edge连接到某个新的城市，便把该城市加入connected中。直到所有的城市都被找到为止。
'''
from collections import defaultdict
import heapq

class Solution(object):
    def minimumCost(self, N, connections):
        edges = defaultdict(list)
        for a, b, cost in connections:
            edges[a].append((cost, b))
            edges[b].append((cost, a))
        # Start with city 1
        connected = set()
        connected.add(1)
        # Add all neighbors of 1
        connections = list(edges[1])
        heapq.heapify(connections)
        sol = -1

        while len(connected) < N:
            if not connections:
                return -1

            cost, neighbor = heapq.heappop(connections)
            if neighbor in connected:
                continue
            connected.add(neighbor)
            sol += cost
            for edge in edges[neighbor]:
                # Only add neighbor cities of neighbor, if not yet connected
                if edge[1] not in connected:
                    heapq.heappush(connections, edge)
        return sol

N = 3
connections = [[1,2,5], [1,3,6], [2,3,1]]
sol = Solution()
print(sol.minimumCost(N, connections))

