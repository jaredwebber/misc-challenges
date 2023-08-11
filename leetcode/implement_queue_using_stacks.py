# https://leetcode.com/problems/implement-queue-using-stacks


class MyQueue:
    first: list[int]
    second: list[int]
    fresh: bool = True

    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        self.fresh = False
        self.first.append(x)

    def pop(self) -> int:
        self.second = []
        for i in range(len(self.first) - 1, -1, -1):
            self.second.append(self.first[i])

        self.first.pop(0)
        self.fresh = False
        return self.second.pop()

    def peek(self) -> int:
        if not self.fresh:
            self.second = []
            for i in range(len(self.first) - 1, -1, -1):
                self.second.append(self.first[i])
            self.fresh = True

        return self.second[len(self.second) - 1]

    def empty(self) -> bool:
        return len(self.first) == 0
