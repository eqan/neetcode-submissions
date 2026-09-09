class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        res = 0
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while fresh > 0 and queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dir:
                    nr, nc = dr + r, dc + c
                    if min(nr, nc) >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            res += 1
        return res if fresh == 0 else -1