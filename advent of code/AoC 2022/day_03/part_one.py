file = open("day_03/input.txt", "r")

line = file.readline()
both = 0
sum = 0

while line:
    first_half = line[0 : int(len(line) / 2)]
    second_half = line[int(len(line) / 2) :]
    seen = []
    for char in first_half:
        if char not in seen and char in second_half:
            seen.append(char)
            if char.isupper():
                both += ord(char) - 65 + 27
            else:
                both += ord(char) - 96
    sum += both
    both = 0

    line = file.readline()

print(sum)

file.close()
