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
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def _add_to_front(self, node):
        curr_front = self.head.next
        curr_front.prev = node
        node.next = curr_front
        node.prev = self.head
        self.head.next = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            node = Node(key, value)
            self._add_to_front(node)
            self.cache[key] = node
            self.size += 1

            if self.size > self.capacity:
                prev = self.tail.prev
                self._remove(prev)
                del self.cache[prev.key]
                self.size-=1


        
    