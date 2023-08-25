# https://leetcode.com/problems/split-strings-by-separator


class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        split_str: list[str] = []
        for i in words:
            split_i: list[str] = i.split(separator)
            for s in split_i:
                if s != "":
                    split_str.append(s)
        return split_str
