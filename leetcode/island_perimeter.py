# https://leetcode.com/problems/island-perimeter/description/


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return self.perimeter(grid, i, j)
        return 0

    def perimeter(self, grid: list[list[int]], row: int, col: int) -> int:
        if (
            row >= 0
            and col >= 0
            and row < len(grid)
            and col < len(grid[0])
            and grid[row][col] == 1
        ):
            grid[row][col] = 2
            perim: int = 0
            if row - 1 < 0 or grid[row - 1][col] == 0:
                perim += 1
            if row + 1 >= len(grid) or grid[row + 1][col] == 0:
                perim += 1
            if col - 1 < 0 or grid[row][col - 1] == 0:
                perim += 1
            if col + 1 >= len(grid[0]) or grid[row][col + 1] == 0:
                perim += 1
            return (
                perim
                + self.perimeter(grid, row - 1, col)
                + self.perimeter(grid, row + 1, col)
                + self.perimeter(grid, row, col - 1)
                + self.perimeter(grid, row, col + 1)
            )
        return 0
