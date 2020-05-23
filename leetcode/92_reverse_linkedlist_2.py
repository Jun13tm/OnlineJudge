'''
92: Reverse Linked List 2 Medium 
    • Complexity:
        ○ O(n); O(1)
    • Topics:
        ○ Linkedlist
    • Related:
        ○ LC206
基于206的Reverse，找到m前一个node，然后执行一个带count的reverse。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverse(head, count):
            prev = None
            curr = head
            for i in range(count):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            head.next = curr
            return prev
        
        if m == n: return head
        
        dummy = ListNode(None)
        dummy.next = head
        curr = dummy
        
        for i in range(m - 1):
            curr = curr.next
        curr.next = reverse(curr.next, n - m + 1)
        
        return dummy.next