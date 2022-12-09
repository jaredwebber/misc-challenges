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
