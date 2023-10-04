# https://leetcode.com/problems/largest-local-values-in-a-matrix/


class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        out: list[list[int]] = [[0 for _ in range(len(grid[0]) - 2)] for _ in range(len(grid) - 2)]

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                out[i - 1][j - 1] = self.max_three_by_three(grid, i, j)

        return out

    def max_three_by_three(self, grid: list[list[int]], row: int, col: int) -> int:
        maximum: int = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                maximum = max(maximum, grid[i][j])
        return maximum
