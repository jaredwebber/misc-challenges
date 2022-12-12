from pprint import pprint
import sys


class Process:
    def __init__(self) -> None:
        self.min_steps = 999999
        self.grid = []
        self.visited = set()
        print(sys.getrecursionlimit())
        sys.setrecursionlimit(2000)

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
        moves = []

    def traverse(self, curr, end, steps):
        self.visited.add((curr[0], curr[1]))
        # print(str(steps) + ", min: " + str(self.min_steps) + ", " + str(curr))
        print("unique pos visited: " + str(len(self.visited)))

        # if len(self.visited) == 120:
        #     for coord in self.visited:
        #         self.grid[coord[0]][coord[1]] = 0

        #     for row in self.grid:
        #         row_out = ""
        #         for val in row:
        #             row_out += str(val) + ", "
        #         print(row_out)

        #     quit()

        if curr == end:
            if steps < self.min_steps:
                self.min_steps = steps
            return

        if steps >= self.min_steps:
            return

        curr_val = self.grid[curr[0]][curr[1]]
        self.grid[curr[0]][curr[1]] = 0

        next_positions = self.prioritize_points(curr, end)
        for pos in next_positions:
            self.traverse(pos, end, steps + 1)

        self.grid[curr[0]][curr[1]] = curr_val

        # curr_val = self.grid[curr[0]][curr[1]]
        # self.grid[curr[0]][curr[1]] = 0

        # right
        # next_pos = [curr[0], curr[1] + 1]
        # if (
        #     self.valid_coords(next_pos)
        #     and curr_val + 1 >= self.grid[next_pos[0]][next_pos[1]]
        # ):
        #     print("going right" + str(next_pos[1]))
        #     self.traverse(next_pos, end, steps + 1)

        # # left
        # next_pos = [curr[0], curr[1] - 1]
        # if (
        #     self.valid_coords(next_pos)
        #     and curr_val + 1 >= self.grid[next_pos[0]][next_pos[1]]
        # ):
        #     self.traverse(next_pos, end, steps + 1)

        # # up
        # next_pos = [curr[0] - 1, curr[1]]
        # if (
        #     self.valid_coords(next_pos)
        #     and curr_val + 1 >= self.grid[next_pos[0]][next_pos[1]]
        # ):
        #     self.traverse(next_pos, end, steps + 1)

        # # down
        # next_pos = [curr[0] + 1, curr[1]]
        # if (
        #     self.valid_coords(next_pos)
        #     and curr_val + 1 >= self.grid[next_pos[0]][next_pos[1]]
        # ):
        #     self.traverse(next_pos, end, steps + 1)

        # self.grid[curr[0]][curr[1]] = curr_val

    def startup(self):
        file = open("input.txt", "r")

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

        # maybe block out starting index?
        self.traverse(start, end, 0)
        print(self.grid)

        # print(self.grid)
        print(self.min_steps)
        file.close()
        sys.setrecursionlimit(1000)


Process().startup()
