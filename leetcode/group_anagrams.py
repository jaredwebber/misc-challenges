# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grouped: dict[str] = {}

        for s in strs:
            key = "".join(sorted(s))
            if not grouped.get(key):
                grouped[key] = []
            grouped[key].append(s)

        out: list[list[str]] = []
        for i in grouped.keys():
            out.append(grouped.get(i))
        return out


class SolutionTwo:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups: dict[str, list[str]] = {}

        for string in strs:
            key: str = str(sorted(string))
            if not groups.get(key):
                groups[key] = []
            groups[key].append(string)

        result: list[list[str]] = []
        for val in groups.values():
            result.append(val)

        return result
