class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = TreeNode(key, val)
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = TreeNode(key, val)
                    return
                curr = curr.right
            else:
                curr.val = val
                return
                

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key == curr.key:
                return curr.val
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val


    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val


    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)
    
    def _remove(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            succ = self._find_min(node.right)
            node.key = succ.key
            node.val = succ.val
            node.right = self._remove(node.right, succ.key)
        return node
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def getInorderKeys(self) -> List[int]:
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

