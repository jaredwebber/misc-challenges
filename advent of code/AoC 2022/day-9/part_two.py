if __name__ == "__main__":

    def update_head(dir: str) -> None:
        if dir == "U":
            rope[0][1] += 1
        elif dir == "R":
            rope[0][0] += 1
        elif dir == "D":
            rope[0][1] -= 1
        elif dir == "L":
            rope[0][0] -= 1

    def update_rope() -> None:
        for knot in range(1, 10):
            if rope[knot - 1][0] == rope[knot][0]:
                # check above and below distances
                if rope[knot - 1][1] - 2 == rope[knot][1]:
                    rope[knot][1] += 1
                elif rope[knot - 1][1] + 2 == rope[knot][1]:
                    rope[knot][1] -= 1
            elif rope[knot - 1][1] == rope[knot][1]:
                # check left and right distances
                if rope[knot - 1][0] - 2 == rope[knot][0]:
                    rope[knot][0] += 1
                elif rope[knot - 1][0] + 2 == rope[knot][0]:
                    rope[knot][0] -= 1
            elif (
                abs(rope[knot - 1][0] - rope[knot][0]) > 1
                or abs(rope[knot - 1][1] - rope[knot][1]) > 1
            ):
                # bottom left diagonal
                if (
                    rope[knot][0] < rope[knot - 1][0]
                    and rope[knot][1] < rope[knot - 1][1]
                ):
                    rope[knot][0] += 1
                    rope[knot][1] += 1
                # bottom right diagonal
                elif (
                    rope[knot][0] > rope[knot - 1][0]
                    and rope[knot][1] < rope[knot - 1][1]
                ):
                    rope[knot][0] -= 1
                    rope[knot][1] += 1
                # top right diagonal
                elif (
                    rope[knot][0] > rope[knot - 1][0]
                    and rope[knot][1] > rope[knot - 1][1]
                ):
                    rope[knot][0] -= 1
                    rope[knot][1] -= 1
                # top left diagonal
                elif (
                    rope[knot][0] < rope[knot - 1][0]
                    and rope[knot][1] > rope[knot - 1][1]
                ):
                    rope[knot][0] += 1
                    rope[knot][1] -= 1

        tail_visited.add(tuple(rope[9]))

    file = open("day-9/input.txt", "r")

    tail_visited = set()  # set of coordinates
    rope = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
    ]
    tail_visited.add(tuple(rope[9]))

    for line in file:
        split_line = line.strip().split(" ")
        dir = split_line[0]
        steps = int(split_line[1])
        for step in range(steps):
            update_head(dir)
            update_rope()

    print(len(tail_visited))

    file.close()
