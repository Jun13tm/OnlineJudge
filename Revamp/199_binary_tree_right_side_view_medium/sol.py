# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        tree = [[root]]
        while True:
            temp = []
            for node in tree[-1]:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if not temp:
                break
            else:
                # Append will append assignment
                # However, at beginning of while loop, temp is assigned to
                # a new empty list. The list temp pointed to before, remained 
                # unchanged, can be accessed through tree list
                tree.append(temp)
        ret = []
        for item in tree:
            ret.append(item[-1].val)
        return ret