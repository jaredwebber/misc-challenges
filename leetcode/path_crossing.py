# https://leetcode.com/problems/path-crossing


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited: set[(int, int)] = set()
        x: int = 0
        y: int = 0

        visited.add((x, y))

        for i in path:
            if i == "N":
                y += 1
            elif i == "S":
                y -= 1
            elif i == "E":
                x += 1
            else:
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False
