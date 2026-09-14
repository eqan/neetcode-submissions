class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        orig_color = image[sr][sc] 
        def dfs(r, c, ROWS, COLS):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or image[r][c] != orig_color:
                return

            image[r][c] = color

            dfs(r+1, c, ROWS, COLS)
            dfs(r, c+1, ROWS, COLS)
            dfs(r-1, c, ROWS, COLS)
            dfs(r, c-1, ROWS, COLS)
            return image
        m, n = len(image), len(image[0])
        return dfs(sr, sc, m, n)
