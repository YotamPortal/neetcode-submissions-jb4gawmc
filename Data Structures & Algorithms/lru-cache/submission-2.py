# double linked list node
class ListNode:
    def __init__(self, k = -1, value = -1, next = None, prev = None):
        self.key = k
        self.val = value
        self.next = next
        self.prev = prev

class LRUCache:

    def insert(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash_list = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hash_list:
            return -1
        self.remove(self.hash_list[key])
        self.insert(self.hash_list[key])
        return self.hash_list[key].val
         

    def put(self, key: int, value: int) -> None:
        if key not in self.hash_list:
            self.hash_list[key] = ListNode(key, value)
        else:
            self.hash_list[key].val = value
            self.remove(self.hash_list[key])
        self.insert(self.hash_list[key])
        if len(self.hash_list) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.hash_list[lru.key]
        
