"""
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

"""

from collections import deque

file = open("day_5/input.txt", "r")

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

        append = []
        for i in range(quantity):
            append.append(stacks[source].popleft())

        append.reverse()

        for item in append:
            stacks[dest].appendleft(item)

final_order = ""
for stack in stacks:
    if len(stack) > 0 and stack is not None:
        final_order += stack.popleft()

print(final_order)

file.close()
