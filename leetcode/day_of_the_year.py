# https://leetcode.com/problems/day-of-the-year/


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))

        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

        if month < 2:
            return day
        elif month < 3:
            return days[month - 2] + day
        else:
            return days[month - 2] + day + (1 if leap_year else 0)
