# https://leetcode.com/problems/number-of-enclaves


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        enclaves: int = 0

        # flood borders of grid
        for i in range(len(grid)):
            if grid[i][0] == 1:
                self.flood(grid, i, 0)
            if grid[i][-1] == 1:
                self.flood(grid, i, len(grid[0]) - 1)
        for i in range(len(grid[0])):
            if grid[0][i] == 1:
                self.flood(grid, 0, i)
            if grid[-1][i] == 1:
                self.flood(grid, len(grid) - 1, i)

        # count remaining enclaves
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 1:
                    enclaves += 1

        return enclaves

    def flood(self, grid: list[list[int]], i: int, j: int) -> None:
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            self.flood(grid, i + 1, j)
            self.flood(grid, i - 1, j)
            self.flood(grid, i, j + 1)
            self.flood(grid, i, j - 1)
