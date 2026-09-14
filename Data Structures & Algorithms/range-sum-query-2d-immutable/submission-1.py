class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0]*(COLS + 1) for _ in range(ROWS + 1)]
        '''
            Think like this, previously we were dealing with only 1 row, now we are going 2D, so in 2D the previous left row has to be accounted as well for the current prefix we are calculating, so we add that up as well
        '''
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c] # Running sum across the current row
                above = self.sumMat[r][c+1] # Accumulate from the above row
                self.sumMat[r+1][c+1] = prefix + above

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        # Adding up 1 so we move onto the actual Rows and Columns rather than including the buffer one
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
        '''
    A diagram to visualise why we are  doing the below
    ┌───────────────┐
    │               │
    │    ▓▓▓▓▓▓▓    │  ← includes stuff we DON'T want
    │    ▓ TARGET ▓ │
    │    ▓▓▓▓▓▓▓    │
    └───────────────┘
    Now if you analuse closely, the top-left corner: the region above row1 and left of col1 got subtracted twice — once by above, once by left.
        So we over removed it, add it back:
        topLeft = sumMat[r1-1][c1-1] — that exact overlapping corner block.
        Mental picture:
        c1-1        c2
         │           │
  ───────┼───────────┤
  r1-1   │  [above]  │   → subtract
  ───────┼───────────┤
         │  TARGET   │
  r2     │           │
  ───────┴───────────┘
         ↑
      [left] → subtract
      corner  → add back
        '''
        bottomRight = self.sumMat[r2][c2]
        above = self.sumMat[r1-1][c2]
        left = self.sumMat[r2][c1 - 1]
        topLeft = self.sumMat[r1-1][c1-1]
        return bottomRight - above - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)