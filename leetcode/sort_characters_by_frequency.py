# https://leetcode.com/problems/sort-characters-by-frequency


class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map: dict[str, int] = {}
        for i in s:
            freq_map[i] = freq_map.get(i, 0) + 1

        result: str = ""
        for char, freq in sorted(freq_map.items(), key=lambda x: x[1], reverse=True):
            result += char * freq

        return result
