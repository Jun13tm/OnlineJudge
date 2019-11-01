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
        dic = {node.val:head}
        
        while len(stack) > 0:
            curr = stack.pop()
            for neighbor in curr.neighbors:
                # New node
                if neighbor.val not in dic:
                    clone = Node(neighbor.val, [])
                    dic[clone.val] = clone
                    # Since not a tree, only add new node to stack, works like visited 
                    stack.append(neighbor)
                # Always connect this neighbor
                dic[curr.val].neighbors.append(dic[neighbor.val])
        return head
