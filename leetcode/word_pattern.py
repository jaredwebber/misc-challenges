# https://leetcode.com/problems/word-pattern


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr: list[str] = s.split(" ")
        if len(pattern) != len(s_arr):
            return False

        pattern_map: dict[str, str] = {}

        for i in range(len(pattern)):
            if pattern_map.get(pattern[i]):
                if pattern_map.get(pattern[i]) != s_arr[i]:
                    return False
            elif s_arr[i] in pattern_map.values():
                return False
            else:
                pattern_map[pattern[i]] = s_arr[i]
        return True
