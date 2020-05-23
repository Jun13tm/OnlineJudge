'''
236: Lowest Common Ancestor of a Binary Tree Medium 
    • Complexity:
        ○ O(n); O(n)
    • Topics:
        ○ binary_tree
把两个target的path找出来，比对就行了。不知为何在leetcode上过不了。nvm
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Find paths for p, q
        def path(root, target):
            # Target
            if root.val == target.val:
                return [target.val]
            # Leaf
            if not root.left and root.right:
                return -1
            if root.left:
                ret = path(root.left, target)
                # if target found, ret is a list
                if isinstance(ret, list):
                    ret.append(root.val)
                    return ret
            if root.right:
                ret = path(root.right, target)
                if isinstance(ret, list):
                    ret.append(root.val)
                    return ret
            # Both children return -1
            return -1
        
        path_p = path(root, p)
        path_q = path(root, q)
        
        # Compare two paths
        set_ = set()
        for val in path_p:
            set_.add(val)
        for val in path_q:
            if val in set_:
                return val