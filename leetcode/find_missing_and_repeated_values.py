# https://leetcode.com/problems/find-missing-and-repeated-values


class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        seen: dict[int, bool] = {}
        total: int = 0
        duplicate: int = -1

        for arr in grid:
            for i in arr:
                if seen.get(i):
                    duplicate = i
                else:
                    total += i
                    seen[i] = True

        expected: int = 0
        for i in range(1, (len(grid) ** 2) + 1):
            expected += i

        return [duplicate, expected - total]
