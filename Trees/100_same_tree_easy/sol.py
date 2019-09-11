# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # DFS Traverse
        def DFS(root, li):
            if root.left == None:
                if root.right != None:
                    li.append(None)
            else:
                DFS(root.left, li)
            li.append(root.val)
            if root.right == None:
                if root.left != None:
                    li.append(None)
            else:
                DFS(root.right, li)
        # Edge cases:
        if p == None and q == None: return True
        if p == None or q == None: return False
        # General case:
        li_p, li_q = [], []
        DFS(p, li_p)
        DFS(q, li_q)
        print(li_p, li_q)
        return True if li_p == li_q else False    