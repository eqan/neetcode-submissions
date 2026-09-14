class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        fresh, queue = 0, deque()
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))
        dirs = [[0, -1], [-1, 0], [1, 0], [0, 1]]
        time = 0
        while queue:
            r, c, length = queue.popleft()
            time = max(time, length)
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if min(nr, nc) >= 0 and nr < R and nc < C and grid[nr][nc] == 1:
                    fresh -= 1
                    grid[nr][nc] = 2
                    queue.append((nr, nc, length + 1))
        return time if fresh == 0 else -1
            
