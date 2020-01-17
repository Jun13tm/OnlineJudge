'''
	• Complexity:
		○ O(n); O(n)
		○ Optimal: O(n); O(1) with weaved list
	• Topics:
		○ Recursion/Iteration
	• Related:
		○ LC133
Recursion和Iteration确保每个node只被克隆一次，根据curr是否在mapping内来判断clone_curr如
何连接。Iterative approach可以记录prev node，在下一个node里再连接，可以少不用检查curr.next
Followup里问到如何达到O(1)的space complexity，可以首先一次遍历将所有的clone node都先克隆
出来，append到各自original node的后面。在第二次遍历做connecting的时候，通过original_node.next
去access clone node，等于是在不用额外space的情况下达到了mapping的效果。
'''

### Iterative ###
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def cloneNode(node, mapping):
            clone = Node(node.val, None, None)
            mapping[node] = clone
            return clone
        
        mapping = {}
        curr, prev = head, None
        while curr:
            if curr in mapping:
                clone = mapping[curr]
            else:
                clone = cloneNode(curr, mapping)
            
            # Connect prev node's clone
            if prev: mapping[prev].next = clone
            
            clone = mapping[curr] if curr in mapping else cloneNode(curr)
            if not curr.random:
                clone.random = None
            elif curr.random in mapping:
                clone.random = mapping[curr.random]
            else:
                clone.random = cloneNode(curr.random, mapping)
            
            prev = curr
            curr = curr.next
        
        if not head:
            return None
        return mapping[head]

### Recursive ###
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # return clone of input node
        def explore(node, mapping):
            if not node:
                return None
            if node in mapping:
                return mapping[node]
            else:
                clone = Node(node.val, None, None)
                mapping[node] = clone
                if node.next:
                    clone.next = explore(node.next, mapping)
                if node.random:
                    clone.random = explore(node.random, mapping)
                return clone
            
        return explore(head, {})
                    
            