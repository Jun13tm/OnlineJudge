"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        head = Node(node.val, [])
        dic = {head.val:head}
        # Only add original nodes to stack 
        stack = [node]
        
        while len(stack) > 0:
            curr = stack.pop()
            clone = dic[curr.val]
            for item in curr.neighbors:
                if item.val not in dic:
                    new = Node(item.val, [])
                    dic[new.val] = new
                    stack.append(item)
                # Always connect
                clone.neighbors.append(dic[item.val]) 
        return head