# https://leetcode.com/problems/unique-number-of-occurrences


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        arr.sort()

        curr_count: int = 1
        occurrences: set[int] = set()
        last: str = arr[0]

        for i in range(1, len(arr)):
            if arr[i] == last:
                curr_count += 1
            else:
                if curr_count in occurrences:
                    return False
                occurrences.add(curr_count)
                curr_count = 1
                last = arr[i]

        return curr_count not in occurrences
