# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        negatives: int = 0
        col_cutoff: int = 0
        row_cutoff: int = 0

        for i in range(len(grid) - 1, -1 + row_cutoff, -1):
            for j in range(len(grid[0]) - 1, -1 + col_cutoff, -1):
                if grid[i][j] < 0:
                    negatives += 1
                else:
                    col_cutoff = j
                    row_cutoff = i

        return negatives
