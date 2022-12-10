import sys


def process() -> None:
    file = open("day-7/input.txt", "r")

    line = file.readline()
    directories = {}
    curr_path = ""

    while line:
        arr = line.strip().split(" ")

        if "cd" in arr:
            if ".." in arr:
                curr_path = curr_path[: curr_path.rindex("/")]
            elif "/" in arr:
                curr_path = ""
            else:
                curr_path += "/" + arr[2]
            line = file.readline().strip()
        elif "ls" in arr:
            line = file.readline().strip()
            dir_total = 0
            if not directories.get(curr_path):  # avoid double counting entire dir
                directories[curr_path] = []
                while line and line.split(" ")[0] != "$":
                    if line.split(" ")[0] == "dir":
                        directories[curr_path].append(
                            curr_path + "/" + line.split(" ")[1]
                        )
                    else:
                        dir_total += int(line.split(" ")[0])
                    line = file.readline().strip()
                directories[curr_path].append(dir_total)

    total_disk = 70000000
    target_free = 30000000
    currently_filled = calc_size("", directories)
    to_delete = target_free - (total_disk - currently_filled)  # target - currently free

    min_over = sys.maxsize
    for d in directories:
        dir_sum = calc_size(d, directories)
        if dir_sum >= to_delete and dir_sum < min_over:
            min_over = dir_sum

    print(min_over)

    file.close()


def calc_size(dir: str, directories: dict) -> int:
    curr_dir = directories.get(dir)

    if not curr_dir:
        return 0
    if len(curr_dir) == 1:
        return int(curr_dir[0])
    else:
        total = 0
        for index in range(len(curr_dir)):
            if type(curr_dir[index]) is str:
                total += calc_size(curr_dir[index], directories)
            else:
                total += curr_dir[index]
        directories[dir] = [total]
        return total


process()
