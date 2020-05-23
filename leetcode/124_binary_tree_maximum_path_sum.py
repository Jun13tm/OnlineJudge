'''
124: Binary Tree Maximum Path Sum Hard
    • Complexity:
        ○ O(n); O(logn)
    • Topics:
        ○ post_order_traversal
        ○ dp
有一点dp的思想，每个node return的是包含当前node.val的最大subpath value。注意在更新全局max
的时候，要考虑root.val + left + right的情况，然而return的时候，不考虑这种情况。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def postTraverse(root):
            nonlocal global_max
            # Leaf
            if not root.left and not root.right:
                if not global_max or root.val > global_max:
                    global_max = root.val
                return root.val
            li, li2 = [root.val], [root.val]
            if root.left:
                left = postTraverse(root.left)
                li.append(root.val + left)
                li2.append(left)
            if root.right:
                right = postTraverse(root.right)
                li.append(root.val + right)
                li2.append(right)
            li.append(sum(li2))
            local_max = max(li)
            if not global_max or local_max > global_max:
                global_max = local_max
            li.pop()
            return max(li)
        
        if not root: return 0
        
        global_max = None
        postTraverse(root)
        return global_max