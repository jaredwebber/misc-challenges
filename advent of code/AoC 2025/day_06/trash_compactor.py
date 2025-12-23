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


def part_two() -> None:
    operators = lines[-1].split()

    numbers = [[] for _ in range(len(operators))]

    column_widths = []
    last_index = 0
    for index, value in enumerate(lines[-1][1:]):
        if value in ops:
            column_widths.append(index - last_index)
            last_index = index + 1

    column_widths.append(len(lines[0]) - last_index)

    for i, val in enumerate(column_widths):
        for _ in range(val):
            numbers[i].append("0")

    for line in lines[:-1]:
        index = 0
        for column, val in enumerate(column_widths):
            for i in range(val):
                numbers[column][i] += line[index] if line[index].isalnum() else ""
                index += 1
            index += 1

    total_sum = 0
    for i in range(len(numbers)):
        sub_calc = 0 if ops[operators[i]] is operator.add else 1

        for j in numbers[i]:
            sub_calc = ops[operators[i]](int(j), sub_calc)

        total_sum += sub_calc

    print(total_sum)


part_two()
