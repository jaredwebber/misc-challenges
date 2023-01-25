# https://leetcode.com/problems/min-stack/description/


class MinStack:
    def __init__(self):
        self.stack: list[(int, int)] = []

    def push(self, val: int) -> None:
        self.stack.append((val, min(self.getMin() if self.stack != [] else val, val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
