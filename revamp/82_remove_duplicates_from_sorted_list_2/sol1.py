# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:        
        # Also update parent, reset count
        def removeNode(count):
            nonlocal parent
            if count == 1:
                parent = parent.next
            else:
                for i in range(count):
                    parent.next = parent.next.next
                
        if not head or not head.next: return head
            
        dummy = ListNode(None)
        dummy.next = head
        curr = head
        curr_val = head.val
        parent = dummy
        count = 1
        
        while curr.next:
            if curr.next.val == curr_val:
                curr = curr.next
                count += 1
            else:
                curr = curr.next
                removeNode(count)
                curr_val = curr.val
                count = 1
        if curr.next == None:
            removeNode(count)
        
        return dummy.next