# https://leetcode.com/problems/rotting-oranges/description/

import queue


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue_: queue[tuple(int)] = queue.Queue()
        remaining_oranges: int = 0
        cycle_count: int = 0

        # populate initial queue
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue_.put((r, c))
                elif grid[r][c] == 1:
                    remaining_oranges += 1

        while remaining_oranges > 0 and not queue_.empty():
            # update all rotten adjacent
            for _ in range(queue_.qsize()):
                x, y = queue_.get()
                if x > 0 and grid[x - 1][y] == 1:
                    remaining_oranges -= 1
                    grid[x - 1][y] = 2
                    queue_.put((x - 1, y))
                if x < len(grid) - 1 and grid[x + 1][y] == 1:
                    remaining_oranges -= 1
                    grid[x + 1][y] = 2
                    queue_.put((x + 1, y))
                if y > 0 and grid[x][y - 1] == 1:
                    remaining_oranges -= 1
                    grid[x][y - 1] = 2
                    queue_.put((x, y - 1))
                if y < len(grid[0]) - 1 and grid[x][y + 1] == 1:
                    remaining_oranges -= 1
                    grid[x][y + 1] = 2
                    queue_.put((x, y + 1))

            cycle_count += 1

        return -1 if remaining_oranges > 0 else cycle_count
