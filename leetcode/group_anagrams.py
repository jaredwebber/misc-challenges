# https://leetcode.com/problems/group-anagrams/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped: dict[str] = {}

        for s in strs:
            key = "".join(sorted(s))
            if not grouped.get(key):
                grouped[key] = []
            grouped[key].append(s)

        out: List[List[str]] = []
        for i in grouped.keys():
            out.append(grouped.get(i))
        return out
