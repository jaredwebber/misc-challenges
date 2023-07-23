# https://leetcode.com/problems/unique-paths-iii


class Solution:
    def __init__(self):
        self.paths = set()
        self.valid_squares = 0

    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        start: list[int]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    self.valid_squares += 1
                    if grid[i][j] == 1:
                        start = [i, j]
        self.traverse(grid, start[0], start[1], "")
        return len(self.paths)

    def traverse(self, grid: list[list[int]], x: int, y: int, path: str) -> None:
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        if grid[x][y] == 2 and len(path) == self.valid_squares - 1:
            self.paths.add(path)
        elif grid[x][y] != -1:
            temp: int = grid[x][y]
            grid[x][y] = -1
            self.traverse(grid, x + 1, y, path + "D")
            self.traverse(grid, x - 1, y, path + "U")
            self.traverse(grid, x, y + 1, path + "R")
            self.traverse(grid, x, y - 1, path + "L")
            grid[x][y] = temp
