from pathlib import Path
import math
import operator

PROJECT_DIR = Path(__file__).parent
path = PROJECT_DIR / "input.txt"
file_content = path.read_text()
lines = file_content.splitlines()

ops = {
    "+": operator.add,
    "*": operator.mul,
}


def part_one() -> None:
    operators = lines[-1].split()

    values = []
    string_vals = lines[0].split()
    for i in string_vals:
        values.append(int(i))

    print(values)

    for line in lines[1 : len(lines) - 1]:
        for i, char in enumerate(line.split()):
            values[i] = ops[operators[i]](int(char), values[i])
    print(values)
    print(sum(values))


# part_one()


# this doesnt work - theres both right and left offsets
# need to include spaces to figure out the digit index

# just read into grid and then parse the grid?


def part_two() -> None:
    operators = lines[-1].split()

    numbers = [[] for _ in range(len(operators))]
    print(numbers)

    for line in lines[0 : len(lines) - 1]:
        for index, num in enumerate(line.split()):
            for i, val in enumerate(reversed(num)):
                if len(num) > len(numbers[index]):
                    temp_index = 0
                    while temp_index < len(num):
                        numbers[index].insert(0, "")
                        temp_index += 1

                digit_index = len(numbers[index]) - i - 1
                # need to fix when digitIndex is negative

                print(i)
                print(val)
                print(digit_index)
                print()

                # print(len(numbers[index]))
                # print(digit_index)

                print(numbers)
                numbers[index][digit_index] += str(val)

                print(numbers)
            print()


# 123 328  51 64
# 45 64  387 23
#  6 98  215 314

# [1, 2, 3]
# [1, 24, 35]
# [1, 24, 356]


part_two()
