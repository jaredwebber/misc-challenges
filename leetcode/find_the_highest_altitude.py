# https://leetcode.com/problems/find-the-highest-altitude


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        largest: int = 0
        total: int = 0

        for i in gain:
            total += i
            largest = max(largest, total)

        return largest
