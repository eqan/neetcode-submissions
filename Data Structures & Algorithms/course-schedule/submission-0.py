class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        visiting, visit = set(), set()
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        def dfs(crc):
            if crc in visiting:
                return False
            if crc in visit:
                return True
            visiting.add(crc)
            for nei in adjList[crc]:
                if not dfs(nei):
                    return False
            visiting.remove(crc)
            visit.add(crc)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            