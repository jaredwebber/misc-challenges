from pathlib import Path

PROJECT_DIR = Path(__file__).parent
path = PROJECT_DIR / "input.txt"
file_content = path.read_text()
lines = file_content.splitlines()

grid: list[list[str]] = [[] for _ in range(len(lines))]

for index, line in enumerate(lines):
    val = line.strip()
    for i in val:
        grid[index].append(i)


def print_grid():
    for i in range(len(grid)):
        print_line = ""
        for j in range(len(grid[0])):
            print_line += grid[i][j]
        print(print_line)


def part_one() -> None:
    splits = 0

    for index, val in enumerate(lines[0]):
        if val == "S":
            grid[1][index] = "|"

    for i in range(2, len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^" and grid[i - 1][j] == "|":
                if j > 0 and grid[i][j - 1] != "^":
                    grid[i][j - 1] = "|"
                if j < len(grid[0]) and grid[i][j + 1] != "^":
                    grid[i][j + 1] = "|"
                splits += 1
            if grid[i - 1][j] == "|" and grid[i][j] == ".":
                grid[i][j] = "|"

    print(splits)
    pass


part_one()
