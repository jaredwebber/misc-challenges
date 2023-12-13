# https://leetcode.com/problems/pacific-atlantic-water-flow


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pacific: list[int] = []
        atlantic: list[int] = []

        for i in range(len(heights)):
            pacific.append((i, 0))
            atlantic.append((i, len(heights[0]) - 1))

        for j in range(len(heights[0])):
            pacific.append((0, j))
            atlantic.append((len(heights) - 1, j))

        reach_pacific: set[int] = self.bfs(pacific, heights)
        reach_atlantic: set[int] = self.bfs(atlantic, heights)

        return list(reach_pacific.intersection(reach_atlantic))

    def bfs(self, queue: list[tuple], heights: list[list[int]]) -> set:
        seen = set()

        while queue:
            x, y = queue.pop(0)
            seen.add((x, y))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (
                    (0 <= x + dx < len(heights))
                    and (0 <= y + dy < len(heights[0]))
                    and (heights[x + dx][y + dy] >= heights[x][y])
                    and (x + dx, y + dy) not in seen
                ):
                    queue.append((x + dx, y + dy))

        return seen
