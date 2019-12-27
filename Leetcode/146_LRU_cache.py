'''
• Complexity:
    ○ O(1) and O(1) for both operations
• Topics:
    ○ design
    ○ linkedlist(double)
这题很适合了解python class/functions的写法。难点在于用double linkedlist去更改某些
key的优先级。hashmap把key->node，linkedlist的front（或者tail）代表list recent。
注意将least recent node pop出去的时候，记得要把该key从cache里也删除。
'''

class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
    
    def __init__(self, capacity: int):
        self.dic = {}
        self.capacity = capacity
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            self.move_to_front(key)
            return self.dic[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].val = value
            self.move_to_front(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
                self.create(key, value)
            else:
                self.evict()
                self.create(key, value)
                
    # Create a new node at the front
    def create(self, key, val):
        node = self.Node(key, val)
        self.dic[key] = node
        
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
    
    # Remove the tail node
    def evict(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        # Remove node from dictionary
        self.dic.pop(node.key)
    
    # Prioritize a node
    def move_to_front(self, key):
        node = self.dic[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head