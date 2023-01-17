# https://leetcode.com/problems/set-matrix-zeroes/description/


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # Do not return anything, modify matrix in-place instead.

        # use row 0 to track column 0s, and column 0 for row 0s,
        # row_zero and col_zero will track values of those columns

        row_zero: bool = False
        col_zero: bool = False

        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                row_zero = True
                break

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col_zero = True
                break

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for r in range(1, len(matrix)):
                    matrix[r][i] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for c in range(1, len(matrix[0])):
                    matrix[i][c] = 0

        if row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        if col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
