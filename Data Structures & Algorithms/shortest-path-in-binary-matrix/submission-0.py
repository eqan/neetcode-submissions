class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        queue = deque()
        visit = set()
        queue.append((0,0,1))
        visit.add((0,0))

        while queue:
            r, c, s = queue.popleft()
            visit.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return s
            edges = [
    [0, 1], [1, 0], [0, -1], [-1, 0],   # cardinal
    [1, 1], [1, -1], [-1, 1], [-1, -1]  # diagonals
]
            for dr, dc in edges:
                nr, nc = dr+ r, dc + c
                if min(nr, nc) < 0 or nr == ROWS or nc == COLS or (nr, nc) in visit or grid[nr][nc] == 1:
                    continue
                queue.append((nr, nc, s + 1))
        return -1

