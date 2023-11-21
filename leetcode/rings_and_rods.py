# https://leetcode.com/problems/rings-and-rods


class Solution:
    def countPoints(self, rings: str) -> int:
        rod_map: dict[int, set] = {}
        for i in range(0, len(rings) - 1, 2):
            rod = int(rings[i + 1])
            if not rod_map.get(rod):
                rod_map[rod] = set()
            rod_map[rod].add(rings[i])

        count: int = 0
        for key, val in rod_map.items():
            if len(val) == 3:
                count += 1

        return count
