# https://leetcode.com/problems/maximum-number-of-balloons


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_map: dict[str, int] = {}
        balloon_chars: list[str] = ["b", "a", "n", "l", "o"]

        for i in balloon_chars:
            balloon_map[i] = 0

        for i in text:
            if i in balloon_chars:
                balloon_map[i] += 1

        min_count: int = 100000
        for i in balloon_chars[:3]:
            min_count = min(min_count, balloon_map.get(i))

        for i in balloon_chars[3:]:
            min_count = min(min_count, int(balloon_map.get(i) / 2))

        return min_count
