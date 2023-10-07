# https://leetcode.com/problems/excel-sheet-column-title/description/


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title: str = ""

        while columnNumber:
            columnNumber -= 1  # minus 1 to get from 1 based A to 0 based A
            title += chr((columnNumber % 26) + 65)
            columnNumber = columnNumber // 26
        return title[::-1]  # reverse string
