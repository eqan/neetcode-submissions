class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def memoize(r, c, ROWS, COLS, cache):
            if r == ROWS or c == COLS:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            cache[r][c] = memoize(r + 1, c, ROWS, COLS, cache) + memoize(r, c + 1, ROWS, COLS, cache)
            return cache[r][c]
            

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return memoize(0, 0, m, n , [[0] * n for _ in range(m) ])
