# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column


class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        row_ones: list[int] = [0 for _ in range(len(grid))]
        row_zeroes: list[int] = [0 for _ in range(len(grid))]
        col_ones: list[int] = [0 for _ in range(len(grid[0]))]
        col_zeroes: list[int] = [0 for _ in range(len(grid[0]))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    row_zeroes[i] += 1
                    col_zeroes[j] += 1
                else:
                    row_ones[i] += 1
                    col_ones[j] += 1

        diff: list[list[int]] = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = row_ones[i] + col_ones[j] - row_zeroes[i] - col_zeroes[j]

        return diff
