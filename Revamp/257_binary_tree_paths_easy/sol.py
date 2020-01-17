# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        #DFS with stack
        if not root: 
            return []
        ret, stack = [], [(root, "")]
        while stack:
            node, string = stack.pop()
            if not node.left and not node.right:
                ret.append(string + str(node.val))
            if node.right:
                stack.append((node.right, string + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, string + str(node.val) + "->"))
        return ret