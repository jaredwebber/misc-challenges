file = open("day_02/input.txt", "r")

line = file.readline()
score = 0

while line:
    if line[0] == "A":
        if line[2] == "X":
            score += 1 + 3
        elif line[2] == "Y":
            score += 2 + 6
        else:
            score += 3 + 0
    elif line[0] == "B":
        if line[2] == "X":
            score += 1 + 0
        elif line[2] == "Y":
            score += 2 + 3
        else:
            score += 3 + 6
    else:
        if line[2] == "X":
            score += 1 + 6
        elif line[2] == "Y":
            score += 2 + 0
        else:
            score += 3 + 3
    line = file.readline()

print(score)

file.close()
