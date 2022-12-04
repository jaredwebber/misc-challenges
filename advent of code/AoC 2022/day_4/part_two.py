"""
--- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""

file = open("day_4/input.txt", "r")

line = file.readline()
count = 0

while line:
    line = line.replace("\n", "")
    split_line = line.split(",")
    first_nums = [int(split_line[0].split("-")[0]), int(split_line[0].split("-")[1])]
    second_nums = [int(split_line[1].split("-")[0]), int(split_line[1].split("-")[1])]

    if (
        first_nums[0] >= second_nums[0]
        and first_nums[0] <= second_nums[1]
        or second_nums[0] >= first_nums[0]
        and second_nums[0] <= first_nums[1]
        or first_nums[0] <= second_nums[0]
        and first_nums[1] >= second_nums[1]
        or second_nums[0] <= first_nums[0]
        and second_nums[1] >= first_nums[1]
    ):
        count += 1
    line = file.readline()

print(count)

file.close()
