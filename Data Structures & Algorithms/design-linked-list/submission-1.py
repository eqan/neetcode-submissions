class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
 
class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.next = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head.next
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.size +=1

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        node = Node(val)
        node.next = self.tail
        curr.next = node
        self.size +=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        node = Node(val)
        node.next  = curr.next
        curr.next = node
        self.size += 1

        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next # skip target node
        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)