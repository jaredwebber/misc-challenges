# https://leetcode.com/problems/count-tested-devices-after-test-operations


class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        count: int = 0
        for percent in batteryPercentages:
            if percent - count > 0:
                count += 1
        return count
