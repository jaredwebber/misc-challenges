# https://leetcode.com/problems/baseball-game


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        total: int = 0
        record: list[int] = []

        for i in operations:
            if i == "+":
                total += record[len(record) - 1] + record[len(record) - 2]
                record.append(record[len(record) - 1] + record[len(record) - 2])
            elif i == "D":
                total += record[len(record) - 1] * 2
                record.append(record[len(record) - 1] * 2)
            elif i == "C":
                total -= record.pop()
            else:
                total += int(i)
                record.append(int(i))

        return total
