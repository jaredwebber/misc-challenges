"""
--- Part Two ---

Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

Delete directory e, which would increase unused space by 584.
Delete directory a, which would increase unused space by 94853.
Delete directory d, which would increase unused space by 24933642.
Delete directory /, which would increase unused space by 48381165.
Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
"""

import sys


def process() -> None:
    file = open("day_7/input.txt", "r")

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
