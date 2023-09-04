# https://leetcode.com/problems/last-day-where-you-can-still-cross


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        low: int = 0
        hi: int = len(cells) - 1
        mid: int = 0
        can_cross: int = 0

        grid: list[list[int]]

        while low <= hi:
            mid = (low + hi) // 2
            grid = self.build_grid(cells, mid, row, col)
            if self.can_cross(row, col, grid):
                can_cross = max(can_cross, mid)
                low = mid + 1
            else:
                hi = mid - 1

        return can_cross

    def build_grid(
        self, cells: list[list[int]], index: int, num_rows: int, num_cols: int
    ) -> None:
        grid: list[list[int]] = [[0 for i in range(num_cols)] for j in range(num_rows)]
        for i in range(index):
            grid[cells[i][0] - 1][cells[i][1] - 1] = 1

        return grid

    def can_cross(self, num_rows: int, num_cols: int, grid: list[list[int]]) -> bool:
        queue: list[list[int]] = []
        row: int
        col: int

        for i in range(num_cols):
            if grid[0][i] == 0:
                queue.append([0, i])

        while len(queue) > 0:
            row, col = queue.pop()
            if row == num_rows - 1 and grid[row][col] == 0:
                return True
            if row > 0 and grid[row - 1][col] == 0:  # up
                queue.append([row - 1, col])
            if col < num_cols - 1 and grid[row][col + 1] == 0:  # right
                queue.append([row, col + 1])
            if row < num_rows - 1 and grid[row + 1][col] == 0:  # down
                queue.append([row + 1, col])
            if col > 0 and grid[row][col - 1] == 0:  # left
                queue.append([row, col - 1])

            grid[row][col] = -1

        return False
