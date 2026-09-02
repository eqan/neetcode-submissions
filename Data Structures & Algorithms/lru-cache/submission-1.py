class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
    
    def _remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def _add_to_front(self, node):
        current_first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = current_first
        current_first.prev = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
        else:
            node = Node(key, value)
            self._add_to_front(node)
            self.cache[key] = node
            self.size+=1
            if self.capacity < self.size:
                node = self.tail.prev
                self._remove(node)
                self.size-=1
                del self.cache[node.key]

    