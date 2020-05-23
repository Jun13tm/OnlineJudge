# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
    • Complexity:
        ○ O(max(m,n)); O(m+n)
    • Topics:
        ○ Linkedlist
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(None)
        curr = ret
        
        carry = 0
        while l1 or l2:
            if l1 and l2:
                su = l1.val + l2.val if not carry else l1.val + l2.val + 1
                l1 = l1.next
                l2 = l2.next
            elif l1:
                su = l1.val if not carry else l1.val + 1
                l1 = l1.next
            else:
                su = l2.val if not carry else l2.val + 1
                l2 = l2.next
            if su >= 10:
                carry = 1
                su -= 10
            else:
                carry = 0
            curr.next = ListNode(su)
            curr = curr.next
        if carry:
            curr.next = ListNode(1)
        return ret.next