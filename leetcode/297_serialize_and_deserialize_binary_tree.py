'''
    • Complexity: 
        ○ O(n); O(n)
    • Topics: 
        ○ dfs
注意这个serialize的方法和leetcode的那个example不一样，不要被迷惑了。DFS很直观，直接把所有的null node也全部encode
到string里。在reconstruct的时候，见到null的话，return None就好了
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Notice this approach is different from the given example
        def dfs(root, ret):
            if not root:
                return ret + "None,"
            # Otherwise add root, then left and right
            ret += str(root.val)
            ret += ","
            ret = dfs(root.left, ret)
            ret = dfs(root.right, ret)
            return ret

        ret = dfs(root, "")
        print(ret)
        return ret
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def reconstruct(li):
            # Base case, return None if null node
            if li[0] == "None":
                li.pop(0)
                return None

            root = TreeNode(li[0])
            li.pop(0)
            root.left = reconstruct(li)
            root.right = reconstruct(li)
            return root
        
        li = data.split(',')
        # Remove trailing empty string
        li.pop()
        return reconstruct(li)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))