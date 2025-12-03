from pathlib import Path
import math

PROJECT_DIR = Path(__file__).parent
path = PROJECT_DIR / "input.txt"
file_content = path.read_text()
lines = file_content.splitlines()


def part_one() -> None:
    position: int = 50
    zeroes: int = 0

    for line in lines:
        instruction: str = line[0]
        count: int = int(line[1:])

        instruction_diff = count % 100

        if instruction == "L":
            if position - instruction_diff < 0:
                position = 100 + (position - instruction_diff)
            else:
                position -= instruction_diff
        else:
            if position + instruction_diff > 99:
                position = (position + instruction_diff) % 100
            else:
                position += instruction_diff

        if position < 0 or position > 99:
            print(position)
            raise Exception("WHAT")

        if position == 0:
            zeroes += 1
    print(f"Part one: {zeroes}")


part_one()


def part_two() -> None:
    position: int = 50
    zeroes: int = 0

    for line in lines:
        instruction: str = line[0]
        count: int = int(line[1:])

        instruction_diff = count % 100

        zeroes += math.floor(count / 100)

        if instruction == "L":
            if position - instruction_diff < 0:
                if position != 0 and 100 + (position - instruction_diff) != 0:
                    zeroes += 1
                position = 100 + (position - instruction_diff)
            else:
                position -= instruction_diff
        else:
            if position + instruction_diff > 99:
                if position != 0 and (position + instruction_diff) % 100 != 0:
                    zeroes += 1
                position = (position + instruction_diff) % 100
            else:
                position += instruction_diff

        if position < 0 or position > 99:
            print(position)
            raise Exception("WHAT")

        if position == 0:
            zeroes += 1

    print(f"Part two: {zeroes}")


part_two()
