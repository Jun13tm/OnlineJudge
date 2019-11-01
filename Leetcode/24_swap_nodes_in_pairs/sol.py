# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(parent, n1):
            n2, child = n1.next, n1.next.next
            parent.next = n2
            n2.next = n1
            n1.next = child
        
        if not head or not head.next: return head
        
        dummy = ListNode(None)
        dummy.next = head
        curr = head
        parent = dummy
        
        while curr and curr.next:
            temp = curr
            swap(parent, curr)
            parent = temp
            curr = temp.next
        
        # Consider Node->None, None-> None, no end case to handle
        return dummy.next
    
"""    
dummy - 1 - 2 - 3 - 4

dummy - 2 - 1 - 3 - 4

dummy - 2 - 1 - 4 - 3 - None
"""    