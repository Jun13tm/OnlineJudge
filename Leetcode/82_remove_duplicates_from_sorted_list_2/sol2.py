# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        def removeNode():
            nonlocal parent
            # Don't remove anynode, but advance parent by 1 node
            if count == 1:
                parent = parent.next
            # Remove count # of nodes
            else:
                for i in range(count):
                    parent.next = parent.next.next
            
        # Main
        if not head or not head.next: return head
        
        dummy = ListNode(None)
        dummy.next = head
        curr = head.next
        parent = dummy
        prev_val = head.val
        count = 1
        
        # Stops at last valid node
        while curr:
            if curr.val == prev_val:
                count += 1
            else:
                removeNode()
                prev_val = curr.val
                count = 1
            curr = curr.next
        # Do one more remove at the end
        removeNode()
        return dummy.next