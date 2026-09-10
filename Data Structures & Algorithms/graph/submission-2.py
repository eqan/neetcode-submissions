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
        if src in self.adjList and dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        return self.dfs(src, dst, set())
    
    def dfs(self, src, dst, visit):
        if src == dst:
            return True
        visit.add(src)
        for neighbor in self.adjList.get(src, set()):
            if neighbor not in visit:
                if self.dfs(neighbor, dst, visit):
                    return True
        return False


