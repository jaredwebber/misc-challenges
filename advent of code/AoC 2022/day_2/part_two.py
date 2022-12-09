file = open("day_2/input.txt", "r")

line = file.readline()
score = 0
ROCK = 1
PAPER = 2
SCISSORS = 3

while line:
    if line[0] == "A":
        if line[2] == "X":
            score += SCISSORS + 0
        elif line[2] == "Y":
            score += ROCK + 3
        else:
            score += PAPER + 6
    elif line[0] == "B":
        if line[2] == "X":
            score += ROCK + 0
        elif line[2] == "Y":
            score += PAPER + 3
        else:
            score += SCISSORS + 6
    else:
        if line[2] == "X":
            score += PAPER + 0
        elif line[2] == "Y":
            score += SCISSORS + 3
        else:
            score += ROCK + 6
    line = file.readline()

print(score)

file.close()
