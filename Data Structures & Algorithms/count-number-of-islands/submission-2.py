class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = 0
        def dfs(r, c, ROWS, COLS):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0' or (r, c) in visit:
                return False
            if grid[r][c] == '1':
                visit.add((r, c))
                dfs(r + 1, c, ROWS, COLS)
                dfs(r, c + 1, ROWS, COLS)
                dfs(r, c - 1, ROWS, COLS)
                dfs(r - 1, c, ROWS, COLS)
                return True
            

        for r in range(ROWS):
            for c in range(COLS):
                res += dfs(r, c, ROWS, COLS)
        return res