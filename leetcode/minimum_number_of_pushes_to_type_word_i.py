# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i


class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_map: dict[str, int] = {}
        for i in word:
            freq_map[i] = freq_map.get(i, 0) + 1

        freq_list = sorted(list(freq_map.items()), key=lambda x: x[1])

        pushes: int = 0
        multiplier: int = 0
        for i in range(len(freq_list)):
            if i % 8 == 0:
                multiplier += 1
            pushes += multiplier * freq_list[i][1]

        return pushes
