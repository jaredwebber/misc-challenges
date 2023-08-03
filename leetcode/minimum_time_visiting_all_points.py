# https://leetcode.com/problems/minimum-time-visiting-all-points


class Solution:
    def min_time_to_visit_all_points(self, points: list[list[int]]) -> int:
        curr: list[int] = points[0]
        time: int = 0
        for i in range(1, len(points)):
            time += self.time_to_move(curr, points[i])
        return time

    def time_to_move(self, start: list[int], end: list[int]) -> int:
        count: int = 0
        while start != end:
            if start[0] == end[0]:  # move vertically
                start[1] += 1 if end[1] > start[1] else -1
            elif start[1] == end[1]:  # move horizontally
                start[0] += 1 if end[0] > start[0] else -1
            elif start[0] < end[0] and start[1] < end[1]:  # move up-right diagonal
                start[0] += 1
                start[1] += 1
            elif start[0] > end[0] and start[1] < end[1]:  # move up-left diagonal
                start[0] -= 1
                start[1] += 1
            elif start[0] > end[0] and start[1] > end[1]:  # move down-left diagonal
                start[0] -= 1
                start[1] -= 1
            else:  # move down-right diagonal
                start[0] += 1
                start[1] -= 1
            count += 1
        return count
