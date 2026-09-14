class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        visit = set()
        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        def dfs(crs):
            # Empty list means its the leaf node
            if len(adjList) <= 0:
                return True
            # We found a cycle!
            if crs in visit:
                return False
            

            # Now running DFS on this particular node and its prereq
            visit.add(crs)
            for nei in adjList[crs]:
                if not dfs(nei):
                    return False
            # We remove the crs from visit after visiting all its nodes to check whether we have a cycle or we reach a leaf node
            visit.remove(crs)
            adjList[crs] = [] # After traversing all the relevant neighbors we delete them
            return True
        # We are going to run dfs for every node
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
            