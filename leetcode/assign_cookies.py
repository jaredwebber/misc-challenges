# https://leetcode.com/problems/assign-cookies


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        g_index: int = 0
        s_index: int = 0

        while g_index < len(g) and s_index < len(s):
            if g[g_index] <= s[s_index]:
                g_index += 1
            s_index += 1

        return g_index
