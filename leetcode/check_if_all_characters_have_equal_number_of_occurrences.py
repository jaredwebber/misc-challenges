# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        map_count: dict[str, int] = {}
        for i in s:
            map_count[i] = map_count.get(i, 0) + 1

        return len(set(map_count.values())) == 1
