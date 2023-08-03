# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage


class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        travel_time: int = 0
        total_garbage: int = 0

        for i in garbage:
            total_garbage += len(i)

        for i in ["M", "P", "G"]:
            time_since_last: int = 0
            for j in range(len(garbage)):
                time_since_last += travel[j - 1] if j > 0 else 0
                if i in garbage[j]:
                    travel_time += time_since_last
                    time_since_last = 0

        return travel_time + total_garbage
