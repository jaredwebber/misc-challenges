if __name__ == "__main__":

    file = open("day_10/input.txt", "r")
    cycle = 0
    cycle_advance = 0
    x = 1
    sum = 0
    ops = {}

    while cycle <= cycle_advance:
        line = file.readline()
        split_line = line.strip().split(" ")

        if cycle in ops:
            x += ops[cycle]

        if split_line != [""]:
            if split_line[0] == "noop":
                cycle_advance += 1
            else:
                ops[cycle_advance + 2] = int(split_line[1])
                cycle_advance += 2

        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220, 260, 300, 340, 380, 420, 460, 500]:
            sum += x * cycle

    print(sum)

    file.close()
