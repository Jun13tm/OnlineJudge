# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(prev, curr):
            next_node = curr.next
            curr.next = prev
            if not next_node:
                return curr
            else:
                return helper(curr, next_node)
        
        # empty linked list & single node         
        if not head or not head.next:
            return head
        next_node = head.next
        head.next = None
        return helper(head, next_node)

