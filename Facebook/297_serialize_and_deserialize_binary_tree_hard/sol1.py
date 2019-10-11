# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def helper(root, ret):
            # Base case
            if not root:
                return ret + "None,"
            # Otherwise left then right 
            ret += str(root.val)
            ret += ','
            ret = helper(root.left, ret)
            ret = helper(root.right, ret)
            return ret
        return helper(root, '')

    def deserialize(self, data):
        def helper(li):
            # Base case
            if li[-1] == 'None':
                li.pop()
                return None
            
            # General case
            root = TreeNode(li[-1])
            li.pop()
            root.left = helper(li)
            root.right = helper(li)
            return root
        li = data.split(',')
        li.reverse()
        root = helper(li)
        return root
        
        
        