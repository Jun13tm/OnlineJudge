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
        
        for i in range(len(li)):
            if i % 2 == 0:
                curr.next = li[i // 2]
            else:
                curr.next = li[-(i // 2 + 1)]
            curr = curr.next
            if i == len(li) - 1:
                curr.next = None
        return dummy.next