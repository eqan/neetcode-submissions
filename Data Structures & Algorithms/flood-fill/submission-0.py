class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        inital_color = image[sr][sc]
        if image[sr][sc] == color:
            return image


        def dfs(grid, r, c):
            ROWS, COLS = len(grid), len(grid[0])

            if min(r, c) < 0 or r == ROWS or c == COLS:
                return
            if grid[r][c] != inital_color:
                return

            grid[r][c] = color
            
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

            return grid
        return dfs(image, sr, sc) 