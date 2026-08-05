class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
       rows, cols = len(grid), len(grid[0])
       perimeter = 0

       for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4

                    # Check top neighbor (2x1 vertical window)
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2

                    # Check left neighbor (1x2 horizontal window)
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2

       return perimeter 
            