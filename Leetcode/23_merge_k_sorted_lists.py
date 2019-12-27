# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
    • Complexity
        ○ O(nlogk) - n being length, k being # of lists
    • Topics
        ○ linkedlist
执行logk次merge2。注意最后merge顺序的书写方法 - 其实可以crappy一点，每次用新的list
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2(l1: ListNode, l2: ListNode):
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
        
        # Edge case handling
        if not lists: return None

        # in-place
        length = len(lists)
        # Current interval
        interval = 1
        while interval < length:
            # Amount - interval makes sure last pair has a distance of interval in between
            for i in range(0, length - interval, interval * 2):
                lists[i] = merge2(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]
        '''
        # Crappy merge (not in place)
        curr = lists
        while len(curr) > 1:
            li = []
            # Actually similar to in-place solution
            for i in range(0, len(curr) - 1, 2):
                li.append(merge2(curr[i], curr[i + 1]))
            # Append the last one if odd
            if len(curr) % 2 == 1:
                li.append(curr[-1])
            curr = li
        return curr[0]
        '''