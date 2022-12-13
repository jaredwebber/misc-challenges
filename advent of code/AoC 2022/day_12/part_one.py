import operator
import sys


class Process:
    def __init__(self) -> None:
        self.min_steps = 999999
        self.grid = []
        self.visited = set()

    def valid_coords(self, coords) -> bool:
        result = (
            coords[0] >= 0
            and coords[1] >= 0
            and coords[0] < len(self.grid)
            and coords[1] < len(self.grid[0])
            and self.grid[coords[0]][coords[1]] != 0
        )
        return result

    def prioritize_points(self, curr, end) -> list[list]:
        move_list = []
        moves = []

        curr_val = self.grid[curr[0]][curr[1]]
        next_positions = [
            [curr[0], curr[1] + 1],
            [curr[0], curr[1] - 1],
            [curr[0] + 1, curr[1]],
            [curr[0] - 1, curr[1]],
        ]

        for next_pos in next_positions:
            if (
                self.valid_coords(next_pos)
                and curr_val + 1 >= self.grid[next_pos[0]][next_pos[1]]
            ):
                x2 = end[0]
                x1 = next_pos[0]
                y2 = end[1]
                y1 = next_pos[1]
                move_list.append(
                    [
                        next_pos,
                        self.grid[next_pos[0]][next_pos[1]],
                        ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5,
                    ]
                )

        # prioritize elevation, then distance to end
        moves = sorted(move_list, key=operator.itemgetter(1))
        moves = sorted(moves, key=operator.itemgetter(2))

        positions = []
        for move in moves:
            positions.append(move[0])

        return positions

    def traverse(self, curr, end, steps):
        self.visited.add((curr[0], curr[1]))

        if curr == end:
            if steps < self.min_steps:
                self.min_steps = steps
            return

        if steps >= self.min_steps:
            return

        next_positions = self.prioritize_points(curr, end)
        curr_val = self.grid[curr[0]][curr[1]]
        self.grid[curr[0]][curr[1]] = 0

        for pos in next_positions:
            self.traverse(pos, end, steps + 1)

        self.grid[curr[0]][curr[1]] = curr_val

    def startup(self):
        file = open("day_12/input.txt", "r")

        start = []
        end = []

        # build grid, load start & end
        for line in file:
            self.grid.append([])
            for char in line.strip():
                if char == "S":
                    start = [len(self.grid) - 1, len(self.grid[len(self.grid) - 1])]
                    self.grid[len(self.grid) - 1].append(ord("a"))
                elif char == "E":
                    end = [len(self.grid) - 1, len(self.grid[len(self.grid) - 1])]
                    self.grid[len(self.grid) - 1].append(ord("z"))
                else:
                    self.grid[len(self.grid) - 1].append(ord(char))

        self.traverse(start, end, 0)

        print(self.min_steps)
        file.close()
        sys.setrecursionlimit(1000)


Process().startup()
