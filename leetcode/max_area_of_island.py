# https://leetcode.com/problems/max-area-of-island/description/


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area: int = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, self.get_area(grid, r, c, 0))
        return max_area

    def get_area(self, grid: list[list[int]], row: int, col: int, area: int) -> int:
        if (
            row >= 0
            and col >= 0
            and row < len(grid)
            and col < len(grid[0])
            and grid[row][col] == 1
        ):
            grid[row][col] = 0
            area += 1
            return (
                area
                + self.get_area(grid, row + 1, col, 0)
                + self.get_area(grid, row - 1, col, 0)
                + self.get_area(grid, row, col + 1, 0)
                + self.get_area(grid, row, col - 1, 0)
            )

        return area
