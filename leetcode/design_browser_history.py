# https://leetcode.com/problems/design-browser-history


class BrowserHistory:
    history: list[str]
    index: int

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.history = self.history[: self.index + 1]
        self.history.append(url)
        self.index = len(self.history) - 1

    def back(self, steps: int) -> str:
        self.index = self.index - steps if self.index - steps >= 0 else 0
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        self.index = (
            steps + self.index
            if steps + self.index < len(self.history)
            else len(self.history) - 1
        )
        return self.history[self.index]
