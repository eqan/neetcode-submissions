class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    def __init__(self, capacity: int):
        self.hashMap = [None] * capacity
        self.capacity = capacity
        self.size = 0
    
    def hash(self, key):
        return key % self.capacity
    

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        while True:
            if self.hashMap[index] == None: # Insert a new item
                self.hashMap[index] = Pair(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.resize()
                return
            elif self.hashMap[index].key == key: # Update the value of an existing item
                self.hashMap[index].val = value
                return
            index+=1
            index = index % self.capacity


    def get(self, key: int) -> int:
        index = self.hash(key)
        while self.hashMap[index] is not None:
            if self.hashMap[index].key == key:
                return self.hashMap[index].val
            index = (index + 1) % self.capacity
        return -1


    def remove(self, key: int) -> bool:
        index = self.hash(key)
        while self.hashMap[index] is not None:
            if self.hashMap[index].key == key:
                self.hashMap[index] = None
                self.size -=1
                return True
            index = (index + 1) % self.capacity
        return False

    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        oldHashMap = self.hashMap
        self.capacity *= 2
        self.hashMap = [None] * self.capacity
        self.size = 0

        for node in oldHashMap:
            if node is not None:
                self.insert(node.key, node.val)
