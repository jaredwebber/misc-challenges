# https://leetcode.com/problems/number-of-employees-who-met-the-target


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        count: int = 0
        for i in hours:
            if i >= target:
                count += 1
        return count
