class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()
        
        def dfs(crs):

            if crs in visit:
                return False
            if preMap[crs] == []:
                return True

            visit.add(crs)

            for nei in preMap[crs]:
                if not dfs(nei): return False

            visit.remove(crs)
            preMap[crs] = []
            return True
        for crs, pre in prerequisites:
            if not dfs(crs):
                return False
        return True

        
