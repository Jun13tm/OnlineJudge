'''
92: Validate BST Medium 
    • Complexity:
        ○ O(n)
    • Topics:
        ○ BST
每个node检查都有upper和lower bound，根据left/right node来update upper/lower就好了。
注意不要用 if not lower/upper，因为这两个值可能为0，另外也注意一下curr_left, curr_right。
另外可以用test = float("inf")来代表INF和neg INF, 避免了上述问题。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(root, lower, upper):                        
            if lower != None and root.val <= lower: 
                return False
            if upper != None and root.val >= upper:
                return False
            
            if root.left:
                curr_upper = root.val if upper == None else min(root.val, upper)
                if not valid(root.left, lower, curr_upper):
                    return False
            if root.right:
                curr_lower = root.val if lower == None else max(root.val, lower)
                if not valid(root.right, curr_lower, upper):
                    return False
            return True
        
        if not root:
            return True
        return valid(root, None, None)