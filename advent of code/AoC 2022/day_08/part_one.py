if __name__ == "__main__":

    def is_visible_from_top(row: int, col: int) -> bool:
        val = grid[row][col]
        row -= 1
        while row >= 0:
            if grid[row][col] >= val:
                return False
            row -= 1
        return True

    def is_visible_from_bottom(row: int, col: int) -> bool:
        val = grid[row][col]
        row += 1
        while row < len(grid):
            if grid[row][col] >= val:
                return False
            row += 1
        return True

    def is_visible_from_left(row: int, col: int) -> bool:
        val = grid[row][col]
        col -= 1
        while col >= 0:
            if grid[row][col] >= val:
                return False
            col -= 1
        return True

    def is_visible_from_right(row: int, col: int) -> bool:
        val = grid[row][col]
        col += 1
        while col < len(grid[0]):
            if grid[row][col] >= val:
                return False
            col += 1
        return True

    file = open("day_08/input.txt", "r")

    grid = []

    # construct grid
    for line in file:
        int_line = []
        for index in line.strip():
            int_line.append(int(index))
        grid.append(int_line)

    # outer ring always visible
    visible = len(grid[0]) * 2 + len(grid) * 2 - 4

    # calculate visible interior
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if (
                is_visible_from_bottom(row, col)
                or is_visible_from_top(row, col)
                or is_visible_from_left(row, col)
                or is_visible_from_right(row, col)
            ):
                visible += 1

    print(visible)

    file.close()

# Incomplete Attempts:
"""
def is_visible(grid: list[list], row: int, col: int, val: int = 0) -> bool:
    print(str(row) + ", " + str(col))
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        print("top false")
        return False

    # outer ring always visible, base case
    if row == 0 or row == len(grid) or col == 0 or col == len(grid[0]):
        print("top true")
        return True

    # check tree is shorter than last
    if val != -1 and val > grid[row][col]:
        print("2nd false")
        return False

    # avoid getting stuck in infinite loop
    # need to track direction we came from
    curr_val = grid[row][col]
    grid[row][col] = -1
    can_be_seen_left = is_visible(grid, row, col - 1, curr_val)
    can_be_seen_right = is_visible(grid, row, col + 1, curr_val)
    can_be_seen_down = is_visible(grid, row - 1, col, curr_val)
    can_be_seen_up = is_visible(grid, row + 1, col, curr_val)

    print("can_be_seen_left: " + str(can_be_seen_left))
    print("can_be_seen_right: " + str(can_be_seen_right))
    print("can_be_seen_down: " + str(can_be_seen_down))
    print("can_be_seen_up: " + str(can_be_seen_up))

    grid[row][col] = curr_val

    return can_be_seen_left or can_be_seen_right or can_be_seen_down or can_be_seen_up


from pprint import pprint


if __name__ == "__main__":
    file = open("day_08/input.txt", "r")

    grid = []

    # construct grid
    for line in file:
        int_line = []
        for index in line.strip():
            int_line.append(int(index))
        grid.append(int_line)

    # outer ring always visible
    visible = len(grid[0]) * 2 + len(grid) * 2 - 4
    visibility_grid = []
    for i in range(len(grid)):
        if i == 0 or i == len(grid) - 1:
            visibility_grid.append([1 for j in range(len(grid[0]))])
        else:
            zeroes = [0 for j in range(len(grid[0]) - 2)]
            visibility_grid.append([1] + zeroes + [1])

    # calculate visible interior
    rows = len(grid)
    cols = len(grid[0])
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            curr_pos = grid[row][col]
            if (
                visibility_grid[row][col - 1] > 0
                and curr_pos > grid[row][col - 1]
                or visibility_grid[row][cols - col] > 0
                and curr_pos > grid[row][cols - col]
            ):
                visibility_grid[row][col] += 1
            if (
                visibility_grid[row - 1][col] > 0
                and curr_pos > grid[row - 1][col]
                or visibility_grid[rows - row][col] > 0
                and curr_pos > grid[rows - row][col]
            ):
                visibility_grid[row][col] += 1

    pprint(visibility_grid)

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if visibility_grid[row][col] > 0:
                print(str(row) + ", " + str(col))
                visible += 1

    print(visible)

    file.close()
"""
