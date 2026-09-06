class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()
        def dfs(grid, r, c, ROWS, COLS, visit, count=0):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r, c))
            count = 1
            count += dfs(grid, r + 1, c, ROWS, COLS ,visit)
            count += dfs(grid, r - 1, c, ROWS, COLS ,visit)
            count += dfs(grid, r, c + 1, ROWS, COLS ,visit)
            count += dfs(grid, r, c - 1, ROWS, COLS ,visit)

            return count
            

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if (r, c) not in visited and grid[r][c] == 1:
                    res = max(dfs(grid, r, c, ROWS, COLS, visited), res)
        return res