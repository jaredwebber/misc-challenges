# https://leetcode.com/problems/design-a-stack-with-increment-operation


class CustomStack:
    max_size: int
    stack: list[int]

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if len(self.stack) > 0 else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(0, min(len(self.stack), k)):
            self.stack[i] += val
