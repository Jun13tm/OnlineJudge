# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
• Complexity:
    ○ O(n); O(1)
• Topics:
    ○ Linkedlist
画一个example比较直观。
'''

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        # Don't need a dummy, since we are returning the tail
        # Use None as prev instead
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev