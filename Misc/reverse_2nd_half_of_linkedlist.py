'''
Reverse right half of a linkedlist Easy 
	• Complexity:
		○ O(n)
	• Topics:
		○ linkedlist
快慢指针找到mid node, 然后mid node.next 进行一下reverse。可以用LC206测试
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def sol(head): 
	def reverse(head):
        if not head: return None
        
        prev = None
        curr = head
        # Stops when current node is None
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev


	if not head: return None

	dummy = ListNode(None)
	dummy.next = head

	# Fast/slow pointers starts at root
	fast, slow = head, head

	# When loop breaks, mid point is found (fast)
	while slow.next and slow.next.next:
		fast = fast.next
		slow = slow.next.next

	fast.next = reverse(fast.next)
	return dummy.next
