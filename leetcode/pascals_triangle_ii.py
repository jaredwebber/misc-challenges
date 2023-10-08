# https://leetcode.com/problems/pascals-triangle-ii


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex < 2:
            return [1 for _ in range(rowIndex + 1)]

        temp: list[int] = []
        last: list[int] = [1, 1]

        for i in range(1, rowIndex):
            temp = [1 for _ in range(len(last) + 1)]
            for j in range(len(last) // 2):
                right_index: int = len(temp) - 2 - j
                temp[j + 1] = last[j] + last[j + 1]
                temp[right_index] = last[right_index] + last[right_index - 1]

            last = temp

        return last
