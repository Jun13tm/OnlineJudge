'''
    • Complexity:
        ○ O(n)
    • Topics:
        ○ DFS/BFS
        ○ Recursion
BFS是natural level order，iterative solution很好写。重点在于如何在输出的list中根据height
划分sublists -- queue的size已经imply了有多少nodes有相同的Heights。直接读代码可能更容易理解
一些。
DFS不管是iterative还是recursive solutions都需要把height传递下去，这样visit node的时候，
该Node知道自己的height是多少。可以用dict (height -> [node_values]）去记录sublists，也可
以在传递height的时候判断是否需要append一个新的sublist。直接读代码。
另外recursive写法最好是把base case和recursive case分开，代码看起来也更elegant。
'''

### BFS ###
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        queue = [root]
        while queue:
            size = len(queue)
            level = []
            # size是固定的，前size个element即是该height的所有Nodes
            for _ in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)

### Recursive DFS ###
from collections import defaultdict

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:        
        def recursion(curr, height, matrix):
            if not curr:
                return 
            # pre/post/in order treverse no difference
            matrix[height].append(curr.val)
            recursion(curr.left, height + 1, matrix)
            recursion(curr.right, height + 1, matrix)

        matrix = defaultdict(list)
        recursion(root, 0, matrix)
        ret = []
        for i in range(len(matrix)):
            ret.append(matrix[i])
        return ret 

### Iterative DFS ###
# 注意append children的顺序是right then left，这样stack才会先visit left then right
from collections import defaultdict

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        matrix = defaultdict(list)
        queue = [(root, 0)]
        while queue:
            curr, height = queue.pop()
            # Read the value
            matrix[height].append(curr.val)
            
            if curr.right:
                queue.append((curr.right, height + 1))
            if curr.left:
                queue.append((curr.left, height + 1))
        ret = []
        for i in range(len(matrix)):
            ret.append(matrix[i])
        return ret