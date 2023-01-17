# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid: list[list[int]] = [[0 for i in range(n)] for j in range(m)]
        grid[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    grid[i][j] += grid[i - 1][j]
                if j > 0:
                    grid[i][j] += grid[i][j - 1]

        return grid[m - 1][n - 1]
