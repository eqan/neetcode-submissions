class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # Brute Force
        def bruteForce(r, c, ROWS, COLS):
            if r == ROWS or c == COLS:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            return bruteForce(r+1, c, ROWS, COLS) + bruteForce(r, c+1, ROWS, COLS)

        # return bruteForce(0, 0, m, n)

        # Top Down - Memoization Approach
        def memoize(r, c, ROWS, COLS, cache):
            if r == ROWS or c == COLS:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            cache[r][c] = memoize(r+1, c, ROWS, COLS, cache) + memoize(r, c+1, ROWS, COLS, cache)
            return cache[r][c]
        

        # return memoize(0, 0, m, n, [[0]* n for i in range(m)])
            
        # Bottom Up Approach - True DP Solution

        def bottomUp(ROWS, COLS):
            prevRow = [0] * COLS
            for r in range(ROWS-1, -1, -1):
                currRow = [0] * COLS
                currRow[COLS-1] = 1
                for c in range(COLS-2, -1, -1): # Keeping COLS-2 because we know last column would have 1 values
                    currRow[c] = currRow[c + 1] + prevRow[c] # We did c+1 i currRow because remember we subtracted -2 initially so getting that value from it
                prevRow = currRow # We replace the previous computed row with the current row and offload the old memory.
            return prevRow[0]


        return bottomUp(m, n)