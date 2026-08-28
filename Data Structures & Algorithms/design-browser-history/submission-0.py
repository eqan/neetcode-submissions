class Node:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.size = 0
        self.curr = Node(homepage)
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def visit(self, url: str) -> None:
        # Create a self looping node at the current position removing all the forward nodes
        node = Node(url, prev=self.curr)
        self.curr.next = node
        self.curr = node
        

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps-=1
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps-=1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)