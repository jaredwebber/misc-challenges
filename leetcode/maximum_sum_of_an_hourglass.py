# https://leetcode.com/problems/maximum-sum-of-an-hourglass


class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        maximum: int = 0

        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                maximum = max(
                    maximum,
                    grid[i][j]
                    + grid[i][j + 1]
                    + grid[i][j + 2]
                    + grid[i + 1][j + 1]
                    + grid[i + 2][j]
                    + grid[i + 2][j + 1]
                    + grid[i + 2][j + 2],
                )
        return maximum
