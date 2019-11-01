# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def DFS(node, li):
            if not node:
                li.append(None)
                return
            li.append(node.val)
            DFS(node.left, li)
            DFS(node.right, li)
        p_li, q_li = [], []
        DFS(p, p_li)
        DFS(q, q_li)
        return False if p_li != q_li else True