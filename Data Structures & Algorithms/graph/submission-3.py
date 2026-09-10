class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList[src]:
            return False
        self.adjList[src].remove(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        return self.dfs(src, dst, set())
    
    def dfs(self, src, dst, visit):
        if src == dst:
            return True
        visit.add(src)
        for nei in self.adjList.get(src, set()):
            if nei not in visit:
                if self.dfs(nei, dst, visit):
                    return True
        return False


