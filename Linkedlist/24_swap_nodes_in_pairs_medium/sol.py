# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 1. Edge checking
        if not head or not head.next:
            return head

        # 2. Add dummy, new_head (ref)
        dummy = ListNode(0)
        dummy.next = head
        new_head = head.next

        prev = dummy    
        first = head
        second = head.next
        next = second.next

        # 3. Iteration
        while(1):
            second.next = first
            prev.next = second
            first.next = next
            # Now check if there are two more nodes to use
            if next and next.next:
                prev = first
                first = prev.next
                second = first.next
                next = second.next
            else:
                break
        return new_head