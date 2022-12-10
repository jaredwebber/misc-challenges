if __name__ == "__main__":

    def update_head(dir: str) -> None:
        if dir == "U":
            head_coords[1] += 1
        elif dir == "R":
            head_coords[0] += 1
        elif dir == "D":
            head_coords[1] -= 1
        elif dir == "L":
            head_coords[0] -= 1

    def update_tail() -> None:
        if head_coords == tail_coords:
            return
        if head_coords[0] == tail_coords[0]:
            # check above and below distances
            if head_coords[1] - 2 == tail_coords[1]:
                tail_coords[1] += 1
            elif head_coords[1] + 2 == tail_coords[1]:
                tail_coords[1] -= 1
        elif head_coords[1] == tail_coords[1]:
            # check left and right distances
            if head_coords[0] - 2 == tail_coords[0]:
                tail_coords[0] += 1
            elif head_coords[0] + 2 == tail_coords[0]:
                tail_coords[0] -= 1
        elif (
            abs(head_coords[0] - tail_coords[0]) > 1
            or abs(head_coords[1] - tail_coords[1]) > 1
        ):
            # bottom left diagonal
            if tail_coords[0] < head_coords[0] and tail_coords[1] < head_coords[1]:
                tail_coords[0] += 1
                tail_coords[1] += 1
            # bottom right diagonal
            elif tail_coords[0] > head_coords[0] and tail_coords[1] < head_coords[1]:
                tail_coords[0] -= 1
                tail_coords[1] += 1
            # top right diagonal
            elif tail_coords[0] > head_coords[0] and tail_coords[1] > head_coords[1]:
                tail_coords[0] -= 1
                tail_coords[1] -= 1
            # top left diagonal
            elif tail_coords[0] < head_coords[0] and tail_coords[1] > head_coords[1]:
                tail_coords[0] += 1
                tail_coords[1] -= 1

        tail_visited.add(tuple(tail_coords))

    file = open("day_09/input.txt", "r")

    tail_visited = set()  # set of coordinates
    head_coords = [0, 0]
    tail_coords = [0, 0]
    tail_visited.add(tuple(tail_coords))

    for line in file:
        split_line = line.strip().split(" ")
        dir = split_line[0]
        steps = int(split_line[1])
        for step in range(steps):
            update_head(dir)
            update_tail()

    print(len(tail_visited))

    file.close()
