file = open("day_1/input.txt", "r")

maximum = 0
count = 0
line = " "

while line:
    line = file.readline()
    if line == "\n" or line == "":
        maximum = max(maximum, count)
        count = 0
    else:
        count += int(line)

print(maximum)

file.close()
