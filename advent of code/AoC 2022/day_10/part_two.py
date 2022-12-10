if __name__ == "__main__":

    file = open("day_10/input.txt", "r")
    cycle = 0
    cycle_advance = 0
    x = 1
    output = ""
    ops = {}
    offset = 0

    while cycle <= cycle_advance and cycle < 240:
        line = file.readline()
        split_line = line.strip().split(" ")

        if cycle in ops:
            x += ops[cycle]

        if cycle in [40, 80, 120, 160, 200, 240, 280]:
            output += "\n"
            offset += 40

        if split_line != [""]:
            if split_line[0] == "noop":
                cycle_advance += 1
            else:
                ops[cycle_advance + 2] = int(split_line[1])
                cycle_advance += 2

        if cycle - offset + 1 == x or cycle - offset == x or cycle - offset - 1 == x:
            output += "#"
        else:
            output += "."

        cycle += 1

    print(output)

    file.close()
