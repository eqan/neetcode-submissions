class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        visit = set()
        res = 0 # Number of islands
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(grid, r, c, ROWS, COLS, visit):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == '0':
                return

            visit.add((r, c))
            dfs(grid, r + 1, c, ROWS, COLS, visit)
            dfs(grid, r - 1, c, ROWS, COLS, visit)
            dfs(grid, r, c + 1, ROWS, COLS, visit)
            dfs(grid, r, c - 1, ROWS, COLS, visit)

        '''
            We iterate through each cell to determine from each cells positions that is a non visited Island or not
        '''
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                '''
                    This is a crucial logic, what is happening here is when we find a grid[i][j] is 1 and the (i, j) is not in visit this means we found an unvisited land and we use the DFS approach to mark the entire land as visited. So next time this condition gets met we know this is a new island
                '''
                if grid[i][j] == '1' and (i, j) not in visit:
                    dfs(grid, i, j, ROWS, COLS, visit)
                    res+=1
        
        return res