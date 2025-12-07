from pathlib import Path
import math

PROJECT_DIR = Path(__file__).parent
path = PROJECT_DIR / "input.txt"
file_content = path.read_text()
lines = file_content.splitlines()


def part_one() -> None:
    total = 0

    for line in lines:
        largest: int = line[0]
        max_joltage = 0

        for val in line[1 : len(line) - 1]:
            if val > largest:
                largest = val
            else:
                joltage = int(str(largest) + str(val))
                if joltage > max_joltage:
                    max_joltage = int(joltage)

        # print(max(max_joltage, int(str(max_joltage) + str(line[-1]))))
        total += max(max_joltage, int(str(largest) + str(line[-1])))

    print(total)


# part_one()


def part_two() -> None:
    total = 0

    for line in lines:
        twelve_largest_values = [0 for _ in range(12)]
        last_index = -1

        for i in range(12):
            for line_index in range(i, len(line) - 12 + i + 1):
                val = line[line_index]
                if last_index < line_index and twelve_largest_values[i] < int(val):
                    twelve_largest_values[i] = int(val)
                    last_index = line_index

        # print(twelve_largest_values)
        total += int("".join(map(str, twelve_largest_values)))

    print(total)


part_two()
