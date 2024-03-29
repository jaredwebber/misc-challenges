# https://leetcode.com/problems/robot-return-to-origin


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x: int = 0
        y: int = 0
        for move in moves:
            if move == "R":
                x += 1
            elif move == "L":
                x -= 1
            elif move == "U":
                y += 1
            else:
                y -= 1

        return x == 0 and y == 0
