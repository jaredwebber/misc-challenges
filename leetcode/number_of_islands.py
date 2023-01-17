# https://leetcode.com/problems/number-of-islands/description/


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands: int = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islands += 1
                    self.flood(row, col, grid)

        return islands

    def flood(self, row: int, col: int, grid: list[list[str]]) -> None:
        if (
            row >= 0
            and col >= 0
            and row < len(grid)
            and col < len(grid[0])
            and grid[row][col] == "1"
        ):
            grid[row][col] = "0"
            self.flood(row + 1, col, grid)
            self.flood(row - 1, col, grid)
            self.flood(row, col + 1, grid)
            self.flood(row, col - 1, grid)
