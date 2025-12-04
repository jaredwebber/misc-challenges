from pathlib import Path
import math

PROJECT_DIR = Path(__file__).parent
path = PROJECT_DIR / "input.txt"
file_content = path.read_text()
ranges = file_content.split(",")


def part_one() -> None:
    invalid_sum = 0

    for range_entry in ranges:
        range_values = range_entry.strip("\n").split("-")
        range_start = int(range_values[0])
        range_end = int(range_values[1])

        for i in range(range_start, range_end + 1):
            id = str(i)

            if id[: math.floor(len(id) / 2)] == id[math.floor(len(id) / 2) :]:
                invalid_sum += i

    print(invalid_sum)


# part_one()


def part_two() -> None:
    invalid_sum = 0

    unique_ids = set()

    for range_entry in ranges:
        range_values = range_entry.strip("\n").split("-")

        for i in range(int(range_values[0]), int(range_values[1]) + 1):
            id = str(i)
            offset = 1

            while offset <= len(id) - 1:
                if len(id) % offset != 0:
                    offset += 1
                    continue
                left: int = 0
                right: int = offset

                while id[left : left + offset] == id[right : right + offset] and right < len(id) - offset:
                    left += offset
                    right += offset

                if id[left : left + offset] == id[right : right + offset] and right == len(id) - offset:
                    unique_ids.add(i)

                offset += 1

    for i in unique_ids:
        invalid_sum += i

    print(invalid_sum)


part_two()
