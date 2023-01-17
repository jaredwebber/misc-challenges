# https://leetcode.com/problems/spiral-matrix/description/


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row: int = 0
        col: int = 0
        order: list[int] = []

        while len(order) < len(matrix) * len(matrix[0]):
            # go right
            for c in range(col, len(matrix[0]) - col):
                if len(order) < len(matrix) * len(matrix[0]):
                    order.append(matrix[row][c])

            # go down
            for r in range(row + 1, len(matrix) - row):
                if len(order) < len(matrix) * len(matrix[0]):
                    order.append(matrix[r][len(matrix[0]) - 1 - col])

            # go left
            for c in range(len(matrix[0]) - col - 2, col, -1):
                if len(order) < len(matrix) * len(matrix[0]):
                    order.append(matrix[len(matrix) - 1 - row][c])

            # go up
            for r in range(len(matrix) - row - 1, row, -1):
                if len(order) < len(matrix) * len(matrix[0]):
                    order.append(matrix[r][col])

            col += 1
            row += 1

        return order
