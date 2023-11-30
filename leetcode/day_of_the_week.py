# https://leetcode.com/problems/day-of-the-week

from datetime import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days: list[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[datetime(year, month, day).weekday()]
