# https://leetcode.com/problems/distance-between-bus-stops


class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        stop: int = max(start, destination)
        start: int = min(start, destination)
        index: int = start

        clockwise: int = 0
        counterclockwise: int = 0

        while index != stop:
            clockwise += distance[index]
            index += 1
            index %= len(distance)

        index = start
        while index != stop:
            index -= 1
            if index < 0:
                index = len(distance) - 1
            counterclockwise += distance[index]

        return min(clockwise, counterclockwise)
