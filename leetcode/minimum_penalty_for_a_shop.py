# https://leetcode.com/problems/minimum-penalty-for-a-shop


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        open_pen: int = 0
        close_pen: int = 0
        open_penalty: list[int] = [0 for i in range(len(customers) + 1)]
        closed_penalty: list[int] = [0 for i in range(len(customers) + 1)]
        for i in range(len(customers) + 1):
            if i < len(customers):
                if customers[i] == "N":
                    open_pen += 1
                if customers[len(customers) - 1 - i] == "Y":
                    close_pen += 1
                open_penalty[i + 1] = open_pen
                closed_penalty[len(customers) - 1 - i] = close_pen

        minimum: int = 1000000
        min_index: int = 0
        for i in range(len(open_penalty)):
            if open_penalty[i] + closed_penalty[i] < minimum:
                minimum = open_penalty[i] + closed_penalty[i]
                min_index = i

        return min_index
