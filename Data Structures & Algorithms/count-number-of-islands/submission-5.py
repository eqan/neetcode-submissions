class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = 0
        def dfs(r, c, ROWS, COLS):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0' or (r, c) in visit:
                return 0
            if grid[r][c] == '1':
                visit.add((r, c))
                dfs(r + 1, c, ROWS, COLS)
                dfs(r, c + 1, ROWS, COLS)
                dfs(r, c - 1, ROWS, COLS)
                dfs(r - 1, c, ROWS, COLS)
                return 1
            
        '''
        We iterate through each cell to determine from each cells positions that is a non visited Island or not
        '''
        for r in range(ROWS):
            for c in range(COLS):
                '''
            This is a crucial logic, what is happening here is when we find a grid[i][j] is 1 and the (i, j) is not in visit this means we found an unvisited land and we use the DFS approach to mark the entire land as visited. So next time this condition gets met we know this is a new island
                '''
                res += dfs(r, c, ROWS, COLS)
        return res