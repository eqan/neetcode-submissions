class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, queue = 0, deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1: # i.e Fresh
                    fresh += 1
                elif grid[i][j] == 2: # i.e Rotten
                    queue.append((i, j, 1))
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c, length = queue.popleft()
                time = max(time, length) # Time is basically the max length we found using the BFS
                for dr, dc, in dir:
                    nr, nc = dr + r, dc + c
                    if min(nr, nc) >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 1: # Checking for inbound only fresh items
                        grid[nr][nc] = 2 # Setting the fresh to rotten aka visited
                        fresh -= 1
                        queue.append((nr, nc, length + 1))
        return time if fresh == 0 else -1
