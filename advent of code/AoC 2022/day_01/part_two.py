file = open("day_01/input.txt", "r")

vals = [0, 0, 0]
count = 0
line = " "

while line:
    line = file.readline()
    if line == "\n" or line == "":
        if count > vals[0]:
            vals[2] = vals[1]
            vals[1] = vals[0]
            vals[0] = count
        elif count > vals[1]:
            vals[2] = vals[1]
            vals[1] = count
        elif count > vals[2]:
            vals[2] = count
        count = 0
    else:
        count += int(line)

print(sum(vals))

file.close()
