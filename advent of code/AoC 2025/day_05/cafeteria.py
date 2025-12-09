from pathlib import Path
import math

PROJECT_DIR = Path(__file__).parent
path = PROJECT_DIR / "input.txt"
file_content = path.read_text()
lines = file_content.splitlines()


fresh_ids_initial = []
ingredients = []

for line in lines:
    if "-" in line:
        first, second = line.split("-")
        fresh_ids_initial.append([int(first), int(second)])
    elif len(line) > 0:
        ingredients.append(int(line.strip()))

ingredients.sort()
fresh_ids_initial.sort()

fresh_ids = [fresh_ids_initial[0]]


for i, (left, right) in enumerate(fresh_ids_initial[1:]):
    if left <= fresh_ids[len(fresh_ids) - 1][0]:
        fresh_ids[len(fresh_ids) - 1][0] = min(fresh_ids[len(fresh_ids) - 1][0], left)
        fresh_ids[len(fresh_ids) - 1][1] = max(fresh_ids[len(fresh_ids) - 1][1], right)

    elif left - 1 <= fresh_ids[len(fresh_ids) - 1][1]:
        fresh_ids[len(fresh_ids) - 1][1] = max(fresh_ids[len(fresh_ids) - 1][1], right)
    else:
        fresh_ids.append([left, right])


def part_one() -> None:
    fresh = 0

    # binary search the fresh_ids ranges to find ingredient id
    for ingredient in ingredients:
        left = 0
        right = len(fresh_ids) - 1
        ingredient_found = False

        while left <= right and not ingredient_found:
            mid = left + ((right - left) // 2)
            if left == right:
                mid = left

            if ingredient >= fresh_ids[mid][0] and ingredient <= fresh_ids[mid][1]:
                fresh += 1
                ingredient_found = True
            elif ingredient < fresh_ids[mid][0]:
                right = mid - 1
            elif ingredient > fresh_ids[mid][1]:
                left = mid + 1

    print(fresh)


part_one()


def part_two() -> None:
    fresh = 0
    for left, right in fresh_ids:
        fresh += right - left + 1

    print(fresh)


part_two()
