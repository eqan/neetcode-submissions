class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1

        # 1. Binary search on rows
        while top <= bot:
            mid_row = (top + bot) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                break   # target is in this row

        if not (top <= bot):
            return False   # row not found

        row = (top + bot) // 2   # the row containing target (if exists)
        l, r = 0, COLS - 1

        # 2. Binary search on columns
        while l <= r:
            mid_col = (l + r) // 2
            if matrix[row][mid_col] < target:
                l = mid_col + 1
            elif matrix[row][mid_col] > target:
                r = mid_col - 1
            else:
                return True

        return False