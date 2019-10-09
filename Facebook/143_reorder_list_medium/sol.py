# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Edge cases
        if not head or not head.next:
            return head
        
        li = [head]
        curr = head
        while curr.next:
            li.append(curr.next)
            curr = curr.next
            
        dummy = ListNode(None)
        curr = dummy
        
        counter = 0
        while True:
            if counter % 2 == 0:
                curr.next = li.pop(0)
            else:
                curr.next = li.pop(-1)
            curr = curr.next
            if len(li) == 0:
                curr.next = None
                break
            counter += 1
        return dummy.next