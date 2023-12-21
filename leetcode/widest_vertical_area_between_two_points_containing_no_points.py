# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points


class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])

        last: int = points[0][0]
        max_diff: int = 0
        for i, _ in points:
            max_diff = max(i - last, max_diff)
            last = i

        return max_diff
