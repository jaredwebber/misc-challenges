from pathlib import Path
import math

PROJECT_DIR = Path(__file__).parent
path = PROJECT_DIR / "input.txt"
file_content = path.read_text()
lines = file_content.splitlines()


grid: list[list[str]] = []

for line in lines:
    curr = []
    for i in line:
        curr.append(i)
    grid.append(curr)


def part_one() -> None:
    accessible = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            adjacent = 0
            if grid[i][j] == "@":
                # top left
                if i > 0 and j > 0 and grid[i - 1][j - 1] == "@":
                    adjacent += 1
                # top
                if i > 0 and grid[i - 1][j] == "@":
                    adjacent += 1
                # top right
                if i > 0 and j + 1 < len(grid[0]) and grid[i - 1][j + 1] == "@":
                    adjacent += 1
                # right
                if j + 1 < len(grid[0]) and grid[i][j + 1] == "@":
                    adjacent += 1
                # bottom right
                if i + 1 < len(grid) and j + 1 < len(grid[0]) and grid[i + 1][j + 1] == "@":
                    adjacent += 1
                # bottom
                if i + 1 < len(grid) and grid[i + 1][j] == "@":
                    adjacent += 1
                # bottom left
                if i + 1 < len(grid) and j > 0 and grid[i + 1][j - 1] == "@":
                    adjacent += 1
                # left
                if j > 0 and grid[i][j - 1] == "@":
                    adjacent += 1

                if adjacent < 4:
                    accessible += 1
    print(accessible)


# part_one()


def part_two() -> None:
    removed = 0
    items_removed = True

    while items_removed:
        items_removed = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                adjacent = 0
                if grid[i][j] == "@":
                    # top left
                    if i > 0 and j > 0 and grid[i - 1][j - 1] == "@":
                        adjacent += 1
                    # top
                    if i > 0 and grid[i - 1][j] == "@":
                        adjacent += 1
                    # top right
                    if i > 0 and j + 1 < len(grid[0]) and grid[i - 1][j + 1] == "@":
                        adjacent += 1
                    # right
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == "@":
                        adjacent += 1
                    # bottom right
                    if i + 1 < len(grid) and j + 1 < len(grid[0]) and grid[i + 1][j + 1] == "@":
                        adjacent += 1
                    # bottom
                    if i + 1 < len(grid) and grid[i + 1][j] == "@":
                        adjacent += 1
                    # bottom left
                    if i + 1 < len(grid) and j > 0 and grid[i + 1][j - 1] == "@":
                        adjacent += 1
                    # left
                    if j > 0 and grid[i][j - 1] == "@":
                        adjacent += 1

                    if adjacent < 4:
                        grid[i][j] = "."
                        removed += 1
                        items_removed = True

    print(removed)


part_two()
