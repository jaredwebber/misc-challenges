if __name__ == "__main__":

    def count_visible_from_top(row: int, col: int) -> int:
        val = grid[row][col]
        count = 0
        row -= 1
        while row >= 0:
            if grid[row][col] >= val:
                return count + 1
            row -= 1
            count += 1
        return count

    def count_visible_from_bottom(row: int, col: int) -> int:
        val = grid[row][col]
        count = 0
        row += 1
        while row < len(grid):
            if grid[row][col] >= val:
                return count + 1
            row += 1
            count += 1
        return count

    def count_visible_from_left(row: int, col: int) -> int:
        val = grid[row][col]
        count = 0
        col -= 1
        while col >= 0:
            if grid[row][col] >= val:
                return count + 1
            col -= 1
            count += 1
        return count

    def count_visible_from_right(row: int, col: int) -> int:
        val = grid[row][col]
        count = 0
        col += 1
        while col < len(grid[0]):
            if grid[row][col] >= val:
                return count + 1
            col += 1
            count += 1
        return count

    def get_scenic_score(row: int, col: int) -> int:
        return (
            count_visible_from_top(row, col)
            * count_visible_from_bottom(row, col)
            * count_visible_from_left(row, col)
            * count_visible_from_right(row, col)
        )

    file = open("day_08/input.txt", "r")

    grid = []

    # construct grid
    for line in file:
        int_line = []
        for index in line.strip():
            int_line.append(int(index))
        grid.append(int_line)

    max = 0

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            scenic_score = get_scenic_score(row, col)
            if scenic_score > max:
                max = scenic_score

    print(max)

    file.close()
