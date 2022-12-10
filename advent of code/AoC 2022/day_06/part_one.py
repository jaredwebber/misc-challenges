# Started on sliding window approach but ran out of time

file = open("day_06/input.txt", "r")

input = file.read()

chunk = []

for i in range(4):
    chunk.append(input[i])

for i in range(4, len(input)):
    if len(set(chunk)) == 4:
        print(i)
        break
    else:
        chunk.pop(0)
        chunk.append(input[i])

file.close()
