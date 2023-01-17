# https://leetcode.com/problems/merge-intervals/description/


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda a: a[0])

        updated_intervals: list[list[int]] = []
        curr_interval: list[int] = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= curr_interval[1]:
                curr_interval[1] = max(curr_interval[1], intervals[i][1])
            else:
                updated_intervals.append(curr_interval)
                curr_interval = intervals[i]

        updated_intervals.append(curr_interval)

        return updated_intervals
