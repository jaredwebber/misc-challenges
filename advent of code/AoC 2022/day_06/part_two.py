file = open("day_06/input.txt", "r")

input = file.read()

chunk = []

for i in range(14):
    chunk.append(input[i])

for i in range(14, len(input)):
    if len(set(chunk)) == 14:
        print(i)
        break
    else:
        chunk.pop(0)
        chunk.append(input[i])


file.close()
