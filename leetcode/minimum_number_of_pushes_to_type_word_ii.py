# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii


class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_map: dict[str, int] = {}
        for i in word:
            freq_map[i] = freq_map.get(i, 0) + 1

        multiplier: int = 0
        count: int = 0
        for index, presses in enumerate(sorted(freq_map.values(), reverse=True)):
            if index % 8 == 0:
                multiplier += 1
            count += presses * multiplier

        return count
