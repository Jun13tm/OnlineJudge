'''
    • Complexity:
        ○ O(n+e) num nodes and edges
    • Topics:
        ○ DFS/BFS
在original graph上做BFS/DFS, 在for neighbor的阶段多一个clone node的步骤，如果存在，gain
access + add edge，如果不存在，create clone node，然后再add edge。注意原图里可能有nodes 
share same value，因此hashmap应该用old node作为key而不是node.val作为key。
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        stack = [node]
        head = Node(node.val, [])
        dic = {node:head}
        
        while stack:
            curr = stack.pop() 
            for neighbor in curr.neighbors:
                if neighbor not in dic:
                    clone = Node(neighbor.val, [])
                    dic[neighbor] = clone
                    stack.append(neighbor)
                # Always connect this neighbor
                dic[curr].neighbors.append(dic[neighbor])
        return head