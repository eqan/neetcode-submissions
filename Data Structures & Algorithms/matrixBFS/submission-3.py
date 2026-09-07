class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # Check if start or end is blocked
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in neighbors:
                    n_r, n_c = r + dr, c + dc
                    if min(n_r, n_c) < 0 or n_r == ROWS or n_c == COLS or (n_r, n_c) in visit or grid[n_r][n_c] == 1:
                        continue
                    queue.append((n_r, n_c))
                    visit.add((n_r, n_c))
            length +=1
        return -1
        