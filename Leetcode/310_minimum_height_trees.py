'''
310: Minimum Height Trees Medium 
    • Complexity: 
        ○ O(n); O(n)
    • Topics: 
        ○ tree
Find max path of a graph using DFS with a fixed root. Then the other end of the 
path is guaranteed to be one end of the whole graph. Find max path with that 
node as the root. The mid nodes make teh minimum height trees.
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Since don't have a node structure ready for use, use dictionary instead
        neighbors = collections.defaultdict(set)
        for v1, v2 in edges:
            neighbors[v1].add(v2)
            neighbors[v2].add(v1)
        
        # Return max path with a givin root
        def maxPath(root, visited):
            visited.add(root)
            paths = [maxPath(neighbor, visited) for neighbor in neighbors[root] if neighbor not in visited]
            print(paths)
            
            path = max(paths or [[]], key=len)
            path.append(root)
            return path
        
        path = maxPath(0, set())
        # Redo with the new root
        path = maxPath(path[0], set())
        max_len = len(path)
        return path[int((max_len - 1) / 2):int(max_len / 2 + 1)]
