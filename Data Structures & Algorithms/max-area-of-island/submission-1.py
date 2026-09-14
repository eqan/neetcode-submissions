class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = 0
        def dfs(r, c, ROWS, COLS):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visit:
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c, ROWS, COLS) + dfs(r, c + 1, ROWS, COLS) + dfs(r, c - 1, ROWS, COLS) + dfs(r - 1, c, ROWS, COLS)
            
        '''
        We iterate through each cell to determine from each cells positions that is a non visited Island or not
        '''
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res = max(res, dfs(r, c, ROWS, COLS))
        return res