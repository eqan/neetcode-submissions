class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N-1][N - 1] == 1:
            return -1
        queue = deque([(0, 0, 1)])
        visit = set([0, 0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [1, -1], [-1, -1], [1, 1]]
        while queue:
            r, c, length = queue.popleft()
            if r == N -1 and c == N - 1:
                return length
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if min(nr, nc) >= 0 and nr < N and nc < N and (nr, nc) not in visit and grid[nr][nc] == 0:
                    queue.append((nr, nc, length + 1))
                    visit.add((nr, nc))
        return -1

