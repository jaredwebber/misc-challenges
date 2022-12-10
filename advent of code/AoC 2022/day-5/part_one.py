from collections import deque

file = open("day-5/input.txt", "r")

stacks = []
read_stacks = True

for line in file:
    if read_stacks:
        if line == "\n":
            read_stacks = False
        elif "[" in line:
            spaces = 0
            new_line = " "
            for char in line:
                if char == " ":
                    spaces += 1
                    if spaces == 4:
                        new_line += "[-]"
                        spaces = 0
                else:
                    new_line += char
                    spaces = 0
                if new_line[-1] == "]":
                    new_line += " "
            chunks = new_line.strip().split(" ")
            for index in range(len(chunks)):
                if len(stacks) == index:
                    stacks.append(deque([]))
                if chunks[index][1] != "-":
                    stacks[index].append(chunks[index][1])
    else:
        split_line = line.split(" ")
        quantity = int(split_line[1])
        source = int(split_line[3]) - 1
        dest = int(split_line[5]) - 1

        for i in range(quantity):
            stacks[dest].appendleft(stacks[source].popleft())

final_order = ""
for stack in stacks:
    final_order += stack.popleft()

print(final_order)

file.close()
