# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:        
        # Given parent
        def removeNode(parent):
            parent.next = parent.next.next
                
        if not head or not head.next: return head
            
        dummy = ListNode(None)
        dummy.next = head
        curr = head
        dic = {head.val:1}
        
        while curr.next:
            if curr.next.val in dic:
                removeNode(curr)
            else:
                dic[curr.next.val] = 1
                curr = curr.next
        
        return dummy.next