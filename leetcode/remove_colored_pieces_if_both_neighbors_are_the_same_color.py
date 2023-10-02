# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) < 3:
            return False

        move_made: bool = False
        start_color: dict[str, int] = {"A": 1, "B": 1}

        while True:
            for color in ["A", "B"]:
                move_made: bool = False
                for i in range(start_color[color], len(colors) - 1):
                    if colors[i - 1] == color and colors[i] == color and colors[i + 1] == color:
                        colors = colors[: i - 1] + colors[i:]
                        start_color[color] = max(1, i - 1)
                        move_made = True
                        break

                if not move_made:
                    return color == "B"
