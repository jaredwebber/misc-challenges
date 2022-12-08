"""
--- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390
Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
The top-middle 5 is visible from the top and right.
The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
The left-middle 5 is visible, but only from the right.
The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
The right-middle 3 is visible from the right.
In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?
"""


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

    file = open("day_8/input.txt", "r")

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
    file = open("day_8/input.txt", "r")

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
