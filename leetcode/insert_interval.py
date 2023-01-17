# https://leetcode.com/problems/insert-interval/description/


class Solution:
    def insert_time_efficient(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        updated_intervals: list[list[int]] = []
        index: int = 0

        # add non-overalapping intervals preceding newInterval
        while index < len(intervals) and (
            intervals[index][0] < newInterval[0]
            and intervals[index][1] < newInterval[0]
        ):
            updated_intervals.append(intervals[index])
            index += 1

        # insert newInterval while considering overlap
        while index < len(intervals) and (
            intervals[index][0] <= newInterval[1]
            or intervals[index][1] <= newInterval[1]
        ):
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1

        updated_intervals.append(newInterval)
        # add remaining intervals
        while index < len(intervals):
            updated_intervals.append(intervals[index])
            index += 1

        return updated_intervals

    def insert_space_efficient(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        index: int = 0

        while index < len(intervals) and (
            intervals[index][0] < newInterval[0]
            and intervals[index][1] < newInterval[0]
        ):
            index += 1

        while index < len(intervals) and (
            intervals[index][0] <= newInterval[1]
            or intervals[index][1] <= newInterval[1]
        ):
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            intervals.pop(index)

        intervals.insert(index, newInterval)

        return intervals
