# https://leetcode.com/problems/positions-of-large-groups/


class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        group_start: int = 0
        group_val: str = s[0]
        large_groups: list[list[int]] = []

        for i in range(1, len(s)):
            if s[i] != group_val:
                if i - group_start >= 3:
                    large_groups.append([group_start, i - 1])
                group_start = i
                group_val = s[i]

        if len(s) - group_start >= 3:
            large_groups.append([group_start, len(s) - 1])

        return large_groups
