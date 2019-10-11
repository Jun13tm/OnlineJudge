# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Approach 1: linkedlist -> list -> sort -> linkedlist -> O(NlogN)
        # Approach 2: compare heads, k comparisons -> O(kN) modify in place O(1)
        # Approach 3: use pq, after poping the largest, insert a new one, log(k) for comparision -> O(Nlogk)
        # Approach 4: merge one by one -> O(kN)
        # Appraoch 5: DnD
        
        # A4 & A5
        if not lists: return None
        if len(lists) == 1: return lists[0]
        
        def merge2(l1, l2):
            # Edge case handling
            if not l1: return l2
            if not l2: return l1

            dummy = ListNode(None)
            curr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            return dummy.next
        
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = merge2(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]