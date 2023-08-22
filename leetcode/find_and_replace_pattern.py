# https://leetcode.com/problems/find-and-replace-pattern


class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        ptt: list[int] = []
        matches: list[str] = []
        pattern_map: dict = {}

        for i in range(len(pattern)):
            ptt.append(self.getPatternValue(pattern_map, pattern[i]))

        index: int
        for i in words:
            index = 0
            pattern_map = {}
            for c in i:
                if ptt[index] != self.getPatternValue(pattern_map, c):
                    index = -1
                    break
                index += 1
            if index != -1:
                matches.append(i)

        return matches

    def getPatternValue(self, map: dict, key: str) -> int:
        if map.get(key):
            return map.get(key)
        map[key] = len(map)
        return len(map)
