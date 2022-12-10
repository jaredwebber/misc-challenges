file = open("day-3/input.txt", "r")

line = file.readline()
lines = [line]
badges = 0

while line:
    if len(lines) == 3:
        in_common = list(set(lines[0]) & set(lines[1]) & set(lines[2]))
        if "\n" in in_common:
            in_common.remove("\n")
        badges += (
            (ord(in_common[0]) - 65 + 27)
            if in_common[0].isupper()
            else (ord(in_common[0]) - 96)
        )
        lines = []
    line = file.readline()
    lines.append(line)

print(badges)

file.close()
