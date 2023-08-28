# https://leetcode.com/problems/furthest-point-from-origin


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counts: list[int] = [0, 0, 0]
        for i in moves:
            if i == "L":
                counts[0] += 1
            elif i == "R":
                counts[2] += 1
            else:
                counts[1] += 1
        return max(counts[0] - counts[2], counts[2] - counts[0]) + counts[1]
